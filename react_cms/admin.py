from django.contrib import admin
from django.db import models

from react_cms.models import ContentResource
from react_cms.models import UploadedFile
from react_cms.widgets import ResourceEditorWidget


class ContentResourceAdmin(admin.ModelAdmin):
    exclude = ('rendered',)
    formfield_overrides = {
        models.TextField: {'widget': ResourceEditorWidget},
    }

    def get_queryset(self, request):
      qs = super(ContentResourceAdmin, self).get_queryset(request)
      user_groups = request.user.groups.filter(name__startswith="mng-")

      if len(user_groups):
        user_countries = [x.name.split('-')[1] for x in user_groups]

        regex = "/("
        for country in user_countries:
          regex += country
        regex += ")/"

        qs = qs.filter(path__iregex=regex)
      return qs

admin.site.register(ContentResource, ContentResourceAdmin)
admin.site.register(UploadedFile)
