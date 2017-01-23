import json
import uuid
from collections import OrderedDict
from django.template.loader import render_to_string
from react_cms.helpers import dict_replace
from django.utils.text import normalize_newlines

class ReactRenderer():
  def __init__(self, json):
    self.json = json
    self.messages = {}
    self.used_uuids = []

  def render(self):
    nodes = json.loads(self.json, object_pairs_hook=OrderedDict)
    components = self._recursive_render(nodes)[0]
    components["messages"] = self.messages
    return json.dumps(components, indent=2)

  def _recursive_render(self, nodes):
    """ Render nodes recursively and return the entire component tree """
    tree = []
    for node in nodes:
      rendered_node = self._render_node(node)
      children = self._recursive_render(node['nodes'])
      rendered_node_with_children = self._render_node_children(rendered_node, children)
      tree.append(rendered_node_with_children)
    return tree

  def _render_node(self, node):
    """ Render a node individually """
    react_component = json.loads(render_to_string('react_cms/react_components/{}.json'.format(node['identifier'])), object_pairs_hook=OrderedDict)
    representation = react_component['representation']
    rendered_node = self._render_props(representation, node)
    return rendered_node

  def _render_props(self, representation, node):
    """ Render node props """
    if 'props' in node:
      for (prop, value) in node['props'].items():
        replace_with = self.filter_value(value)
        prop_uuid = False

        if 'messages' in node:
          for (language, content) in node['messages'].items():
            if prop in content:
              if prop_uuid == False:
                prop_uuid = self._generate_uuid()
                replace_with = "{{%s}}" % prop_uuid
                self._add_prop_to_messages('$default', prop_uuid, value)

              self._add_prop_to_messages(language, prop_uuid, content[prop])


        representation = dict_replace(representation, "@{}".format(prop), replace_with)
    return representation

  def _render_node_children(self, node, children):
    """ Render children inside node """
    node_json = json.dumps(node)
    children_json = json.dumps(children)
    node_with_children = node_json.replace('["@@children"]', children_json)
    return json.loads(node_with_children, object_pairs_hook=OrderedDict)

  def _add_prop_to_messages(self, language, uuid, value):
    lc_language = language.lower()
    if lc_language not in self.messages:
      self.messages[lc_language] = {}

    self.messages[lc_language][uuid] = value

  def _generate_uuid(self):
    # I'll probably have won the lottery when this happens
    # but just in case...
    while True:
      u = str(uuid.uuid4())
      if u not in self.used_uuids:
        self.used_uuids.append(u)
        break
    return u

  def filter_value(self, value):
    """ Apply filters. """
    v = normalize_newlines(value)
    return v.replace("\n", "<br />")
