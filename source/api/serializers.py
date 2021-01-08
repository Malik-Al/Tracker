from rest_framework import serializers
from webapp.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    product = TaskSerializer(many=True, source='projects')

    class Meta:
        model = Project
        fields = '__all__'


