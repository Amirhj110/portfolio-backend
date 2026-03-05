from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    
    # THIS IS THE MISSING LINE:
    serializer_class = ProjectSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'id']

    # This connects the project to the user who is logged in
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)