from ninja import NinjaAPI, Schema
from .models import TaskResult
from ninja.security import django_auth

api = NinjaAPI()

class FileSchema(Schema):
    name: str
    download_link: str

@api.get("/files", response=list[FileSchema], auth=django_auth)
def get_files(request):
    """
    Fetch files for the currently authenticated user and return them in a structured JSON format.
    """
    files = TaskResult.objects.filter(user=request.user).order_by('-created_at')
    return [{"name": file.name, "download_link": file.download_link} for file in files]
