from django.shortcuts import render,HttpResponse, redirect
from .forms import UploadFileForm
from .models import UploadedFile, UploadedFilePydantic
# Assume your utility functions are here
from django.contrib.auth.decorators import login_required
import os
from ninja import NinjaAPI
from ninja import Schema
from ninja import File, Form
from ninja.files import UploadedFile
from myapp.api import api

api = NinjaAPI(version='2.0.0')
# Create your views here.
def home(request):
    return render(request, 'index.html')

def faq(request):
    return render(request, 'faq.html')

def file_upload(request):
    return render(request, 'file-upload.html')

def pricing(request):
    return render(request, 'pricing.html')

def progress(request):
    return render(request, 'progress.html')

def signin(request):
    return render(request, 'signin.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import UploadFileForm
from .models import UploadedFile, CSVFile, ProcessingState
import os
from .models import TaskResult
from celery import chain
from .tasks import process_file
from celery.result import AsyncResult
from django.http import HttpResponseNotFound, JsonResponse, Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UploadedFileSerializer

def home(request):
    return render(request, 'index.html')

class UploadSchema(Schema):
    file: UploadedFile
    
from django.http import JsonResponse
from .models import UploadedFile
from django.core.files.uploadedfile import UploadedFile as DjangoUploadedFile
from myapp.tasks import process_file




@api.post("/upload")
def file_upload_view(request):
    file = request.FILES.get('file')
    if not file:
        return JsonResponse({"message": "No file uploaded"}, status=400)
    
    uploaded_file_instance = UploadedFile(user_id=request.user.id, file=DjangoUploadedFile(file))
    uploaded_file_instance.save()  # Save the instance first to generate the file path

    file_path = uploaded_file_instance.file.path
    file_id = uploaded_file_instance.id
    user_id = request.user.id  # Adjust as necessary for your user identification logic

    task = process_file.delay(file_id, user_id)
    uploaded_file_instance.task_id = task.id  # Store the task_id in the model
    uploaded_file_instance.save()  # Save the model instance
    uploaded_file_instance.output_file_path = file_path
    uploaded_file_instance.save()

    return JsonResponse({"message": "File uploaded successfully", "task_id": task.id})



from django.urls import reverse



@api.get('/task-progress/<str:task_id>')
def task_progress(request, task_id):
    try:
        task_result = TaskResult.objects.get(task_id=task_id)
        response_data = {
            'state': task_result.status,
            'progress': {
                'current': task_result.progress,
                'total': 100,
                'percent': task_result.progress,
            },
            'status': task_result.status,
            'task_completed': task_result.status == 'SUCCESS',
            'outputFile': None
        }

        if task_result.status == 'SUCCESS' and task_result.output_file:
            download_url = request.build_absolute_uri(reverse('download_file', args=[task_result.output_file]))
            response_data['outputFile'] = download_url

        return JsonResponse(response_data)
    except TaskResult.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)


from django.http import FileResponse
from django.conf import settings

def download_file(request, task_id):
    task_result = TaskResult.objects.get(task_id=task_id)
    file_path = task_result.result['file_path']
    file_name = task_result.result['file_name']
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response


@login_required
def check_login(request):
    user = request.user
    data = {
        'isLoggedIn': user.is_authenticated,
        'userName': user.username
    }
    return JsonResponse(data)

from .serializers import FileSerializer
from rest_framework import generics, status
import logging

logger = logging.getLogger(__name__)

class FileSchema(Schema):
    id: int
    name: str

@api.get("/files", response=list[FileSchema])
def get_files(request):
    files = TaskResult.objects.filter(user=request.user).order_by('-created_at')
    file_data = []
    for file in files:
        if file.output_file:
            file_data.append({
                "id": file.id,
                "name": str(file.output_file),
            })
    return file_data

@api.get("/files/{file_id}", response=FileSchema)
def download_file(request, file_id: int):
    file = TaskResult.objects.get(id=file_id, user=request.user)
    if file.output_file:
        response = HttpResponse(file.output_file.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{file.output_file.name}"'
        return response
    else:
        return HttpResponse(status=404)