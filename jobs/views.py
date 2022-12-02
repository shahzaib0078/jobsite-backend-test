from rest_framework import viewsets, mixins
from .models import Job
from .serializers import JobSerializer


class JobViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves user accounts
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer
