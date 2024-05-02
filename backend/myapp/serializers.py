from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'user', 'file', 'created_at']

 # serializers.py
from rest_framework import serializers
from .models import TaskResult

class FileSerializer(serializers.ModelSerializer):
    download_link = serializers.SerializerMethodField()

    class Meta:
        model = TaskResult
        fields = ['id', 'task_id', 'user_id', 'result', 'download_link', 'created_at']

    def get_download_link(self, obj):
        return f"/download/{obj.task_id}/"

    def to_representation(self, instance):
        representation = super(FileSerializer, self).to_representation(instance)
        representation['name'] = instance.result.get('file_name', '') if instance.result else ''
        return representation