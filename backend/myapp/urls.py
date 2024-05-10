from django.urls import path
from . import views
from .views import api, check_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('file-upload/', views.file_upload_view, name='file_upload'),
    path('pricing/', views.pricing, name='pricing'),
    path('progress/', views.progress, name='progress'),
    path('signin/', views.signin, name='signin'),
    path('upload/', views.file_upload_view, name='file_upload1'),
    path('api/check-login/', views.check_login, name='check_login'),
    path('api/', api.urls),
    path('download/<path:file_path>', views.download_file, name='download_file'),
    path('check-login/', check_login, name='check_login'),
    path('api/files/', views.get_files, name='file-list'),  # Update the URL pattern
    path('api/files/<int:file_id>/', views.download_file, name='file-download'),
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),


]