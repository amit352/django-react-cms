import os
import json

from django.forms.widgets import Widget
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template import Context
from django.template.loader import render_to_string
from django.template.loaders.app_directories import get_app_template_dirs
from collections import OrderedDict

class ResourceEditorWidget(Widget):
  template_name = 'react_cms/widgets/resource_editor.html'

  def render(self, name, value, attrs=None, renderer=None):
    context = Context({'value': mark_safe(value),
                       'available_languages': mark_safe(self.get_available_languages()),
                       'components_json': mark_safe(json.dumps(self.build_available_components()))})
    return mark_safe(render_to_string(self.template_name, context))

  def build_available_components(self):
    components = []
    templates = self.get_component_list()

    for template in templates:
      t = json.loads(render_to_string('react_cms/react_components/{}'.format(template)), object_pairs_hook=OrderedDict)
      components.append(self.prepare_component(t["info"]))

    return components

  def prepare_component(self, component):
    if 'props' not in component:
      component['props'] = {}
      for editable_prop in component['editableProps']:
        component['props'][editable_prop] = ''

    return component


  def get_component_list(self):
    template_dir_list = []
    for each in get_app_template_dirs('templates'):
      template_dir_list.append(each)

    template_list = []
    for each in (template_dir_list + settings.TEMPLATES[0]['DIRS']):
      for dir, dirnames, filenames in os.walk(each):
        for filename in filenames:
          path = os.path.join(dir, filename)
          if "react_cms/react_components" in path and "json" in path:
            if filename not in template_list:
              template_list.append(filename)
            else:
              raise RuntimeError("Multiple react components named {} found. Rename one of them.".format(filename))

    return template_list

  def get_available_languages(self):
    languages = settings.LANGUAGES
    #return [x[0] for x in languages]
    return ['pt-BR', 'es-ES']
