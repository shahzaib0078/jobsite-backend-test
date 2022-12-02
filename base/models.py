"""Module contains models for base app."""

from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Parameter(models.Model):
    parameters = models.JSONField(null=True, blank=True)

    class Meta:
        abstract = True
