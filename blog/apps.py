from django.apps import AppConfig
from rest_framework import serializers


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
