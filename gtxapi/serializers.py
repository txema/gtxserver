__author__ = 'txema'
from rest_framework import serializers
from gtxapi.models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.Field(source='created_by.username')
    owner = serializers.Field(source='owner.username')
    tags = serializers.PrimaryKeyRelatedField(many=True)
    statuses = serializers.RelatedField(many=True)

    class Meta:
        model = Task
        fields = ('description', 'created_at', 'updated_at', 'created_by', 'owner', 'tags', 'statuses')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks_assigned = serializers.PrimaryKeyRelatedField(many=True)
    tasks_created = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks_assigned', 'tasks_created')



