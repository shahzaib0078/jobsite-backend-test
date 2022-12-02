"""Module contains models for advertisements app."""

from django.db import models

from websites.models import Website


class Advertisement(models.Model):
    link = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # Status
    status = models.BooleanField(default=False)

    # Foreign Key
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
