import os

from django.conf import settings
from django.template.loaders.app_directories import get_app_template_dirs

class ComponentFinder():
  def find(self):
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
