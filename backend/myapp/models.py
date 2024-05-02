from django.db import models
from django.contrib.auth.models import User
from pydantic import BaseModel, Field, create_model
from typing import Any

# Create your models here.
class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Provide a valid default user ID
    file = models.FileField(upload_to='uploaded_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    output_file = models.FileField(upload_to='output_files/', null=True, blank=True)

    @classmethod
    def __get_pydantic_core_schema__(cls, handler):
        fields = {
            'id': (int, ...),
            'user': (int, ...),
            'file': (str, ...),
            'uploaded_at': (str, ...),
        }
        return create_model(cls.__name__, **fields).__pydantic_core_schema__


class UploadedFilePydantic(BaseModel):
    file: Any

    class Config:
        arbitrary_types_allowed = True


class CSVFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_file = models.ForeignKey(UploadedFile, on_delete=models.SET_NULL, null=True, blank=True, related_name='processed_csvs')
    file = models.FileField(upload_to='processed_csvs/')
    created_at = models.DateTimeField(auto_now_add=True)
    processing_state = models.CharField(max_length=20, default='pending')


class ProcessingState(models.Model):
    file = models.OneToOneField(UploadedFile, on_delete=models.CASCADE, related_name='processing_state')
    state = models.CharField(max_length=100, default='pending')  # Track processing state (e.g., pending, processing, completed)
    processed_file = models.FileField(upload_to='processed_files/', null=True, blank=True)  # Optional: link to processed file
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Processing state for {self.file.file.name}: {self.state}"
    
class TaskResult(models.Model):
    task_id = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    progress = models.IntegerField(default=0)
    output_file = models.FileField(upload_to='output_files/', null=True, blank=True)
    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)