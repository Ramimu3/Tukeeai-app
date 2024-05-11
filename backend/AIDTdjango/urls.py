"""
URL configuration for AIDTdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from myapp.api import api
from myapp.views import file_upload_view, task_progress, download_file
from api.api import api
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("myapp.urls")),
    path('', include('authentication.urls')),
    path('', include('frontend.urls')),
    path("api/", api.urls),
    path('stripe/', include('stripe_integration.urls')),
    path('api/task-progress/<str:task_id>/', task_progress, name='task_progress'),
    path('celery-progress/', include('celery_progress.urls')),  # the endpoint is configurable
    path('accounts/', include('allauth.urls')),
    path('api/upload', file_upload_view, name='file_upload'),
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password/reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
