from django.db import models
from react_cms.renderers import ReactRenderer

class ContentResource(models.Model):
  name = models.CharField("Resource Name", max_length=100)
  path = models.CharField("Resource Path", max_length=1000)
  json = models.TextField("Components", blank=True, null=True)

  def __str__(self):
    return "{} - {}".format(self.name, self.path)

  def save(self):
    super(ContentResource, self).save()

    rendered = ReactRenderer(self.json).render()
    print(rendered)

    f = open('out', 'w')
    f.write(rendered)
    f.close()


    import requests
    r = requests.post("http://localhost:3000/api/cms/update", {"resourcePath": self.path})
    import pudb;pudb.set_trace()

