from django.contrib import admin
from django.db import models

from react_cms.models import ContentResource
from react_cms.widgets import ResourceEditorWidget


class ContentResourceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': ResourceEditorWidget},
    }

admin.site.register(ContentResource, ContentResourceAdmin)
