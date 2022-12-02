from rest_framework import viewsets, mixins
from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves user accounts
    """

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
