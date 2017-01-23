from django.conf.urls import url

from react_cms import views

urlpatterns = [
  url("^content-resources/", views.fetch_resource, name="fetch-resource"),
]
