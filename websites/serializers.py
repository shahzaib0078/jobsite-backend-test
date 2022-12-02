from rest_framework import serializers
from .models import Website


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = (
            "id",
            "name",
            "url",
            "description",
        )
