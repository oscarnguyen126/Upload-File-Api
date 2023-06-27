from rest_framework import serializers
from .models import UploadedFile


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('file', 'uploaded_on', 'target_id', 'target_class')
        
    def create(self, validated_data):
        return UploadedFile.objects.create(**validated_data)
