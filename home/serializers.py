from rest_framework import serializers
from .models import Note
#Note API with ModelViewSet


class MenuCategorySerializer(serializer.ModelSerializer):
    class Meta:
        model= MenuCategorySerializer
        field=['name']



class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
