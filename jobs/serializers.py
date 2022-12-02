from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "job_type",
            "short_description",
            "tags",
            "experience_level",
            "salary_range",
            "location",
            "zip_code",
            "source",
            "source_link",
            "job_status",
            "website",
        )
