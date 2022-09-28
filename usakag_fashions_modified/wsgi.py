"""
WSGI config for usakag_fashions_modified project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
import django
from django.core.handlers.wsgi import WSGIHandler


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "usakag_fashions_modified.settings.production")
django.setup(set_prefix=False)

application = WSGIHandler()
