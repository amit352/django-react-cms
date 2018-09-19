import json

from django.forms.widgets import Widget
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from collections import OrderedDict

from react_cms.finders import ComponentFinder

class ResourceEditorWidget(Widget):
  template_name = 'react_cms/widgets/resource_editor.html'

  def render(self, name, value, attrs=None, renderer=None):
    context = {'value': mark_safe(value),
                       'available_languages': mark_safe(self.get_available_languages()),
                       'strip_parameters': self.get_strip_parameters(),
                       'components_json': mark_safe(json.dumps(self.build_available_components()))}
    return mark_safe(render_to_string(self.template_name, context))

  def build_available_components(self):
    components = []
    templates = ComponentFinder().find()

    for template in templates:
      try:
        t = json.loads(render_to_string('react_cms/react_components/{}'.format(template)), object_pairs_hook=OrderedDict)
      except ValueError as e:
        raise ValueError("Failed decoding JSON on react_cms/react_components/{}. {}".format(template, e))
      components.append(self.prepare_component(t["info"]))

    return components

  def prepare_component(self, component):
    if 'props' not in component:
      component['props'] = {}
      for editable_prop in component['editableProps']:
        component['props'][editable_prop] = ''

    return component

  def get_available_languages(self):
    languages = list(settings.LANGUAGES)
    languages.pop(0) # First language is default
    return [x[0] for x in languages]

  def get_strip_parameters(self):
    s = getattr(settings, 'REACT_CMS', {})
    strip = s.get('STRIP_PARAMETERS_FROM_FILE_URL', False)
    return 'true' if strip else 'false'
