"""Module contains models for jobs app."""

from django.db import models

from websites.models import Website


class Job(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    job_type = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.CharField(max_length=20, null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    experience_level = models.CharField(max_length=255, null=True, blank=True)
    salary_range = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=20, null=True, blank=True)
    source_link = models.CharField(max_length=20, null=True, blank=True)

    # Status
    job_status = models.BooleanField(default=False)

    # Foreign Key
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
