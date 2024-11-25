from rest_framework import viewsets
from .models import Activity, StudentActivity
from .serializers import ActivitySerializer, StudentActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class StudentActivityViewSet(viewsets.ModelViewSet):
    queryset = StudentActivity.objects.all()
    serializer_class = StudentActivitySerializer
