"""Module contains models for website app."""

from django.db import models


class Website(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
