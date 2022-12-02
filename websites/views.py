from rest_framework import viewsets, mixins
from .models import Website
from .serializers import WebsiteSerializer


class WebsiteViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves user accounts
    """

    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
