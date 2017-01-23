from collections import OrderedDict
from django.conf import settings

def rep(value, find, replace):
  if isinstance(value, str):
    value = value.replace(find, replace)
  if isinstance(value, dict) or isinstance(value, OrderedDict):
    value = dict_replace(value, find, replace)
  if isinstance(value, list) or isinstance(value, tuple):
    for i, v in enumerate(value):
      value[i] = rep(v, find, replace)
  return value

def dict_replace(dictionary, find, replace):
  """ Find and replace values inside a dictionary """
  for (key, value) in dictionary.items():
    dictionary[key] = rep(value, find, replace)
  return dictionary

def get_settings(string="REACT_CMS"):
  return getattr(settings, string, {})
