from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    # This ensures the API doesn't ask the user to provide an owner ID
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_at', 'owner']