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

admin.site.register(ContentResource, ContentResourceAdmin)
admin.site.register(UploadedFile)
