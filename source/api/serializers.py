from rest_framework import serializers
from webapp.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'project')


class ProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


