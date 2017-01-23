from django.db import models
from react_cms.renderers import ReactRenderer
import requests

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class ContentResource(models.Model):
  name = models.CharField("Resource Name", max_length=100)
  path = models.CharField("Resource Path", max_length=1000)
  json = models.TextField("Components", blank=True, null=True)
  rendered = models.TextField("Rendered component", blank=True, null=True)

  def __str__(self):
    return "{} - {}".format(self.name, self.path)

  def save(self):
    self.rendered = ReactRenderer(self.json).render()
    super(ContentResource, self).save()

@receiver(post_save, sender=ContentResource, dispatch_uid="notify_client")
def notify_client(sender, instance, **kwargs):
  def on_commit():
    r = requests.post("http://localhost:3000/api/cms/update", {"resourcePath": instance.path})
  transaction.on_commit(on_commit)


class UploadedFile(models.Model):
  title = models.CharField("Title", max_length=200, null=True, blank=True)
  file = models.FileField(upload_to="cms/files")

  def __str__(self):
    return "{} - {}".format(self.title, self.file)

