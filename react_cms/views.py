from django.http import HttpResponse
from react_cms.models import ContentResource
from django.shortcuts import get_object_or_404

def fetch_resource(request):
  path = request.GET.get('path', '')

  if path:
    resource = get_object_or_404(ContentResource, path=path)

  return HttpResponse(resource.rendered, content_type="application/json")
