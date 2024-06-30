from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['completed']
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticated]
