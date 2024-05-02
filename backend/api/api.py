from ninja import NinjaAPI
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError

api = NinjaAPI(version='3.0.0')

@api.post("/login")
def login_view(request, username: str, password: str):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return {"success": True}
    else:
        return {"success": False, "error": "Invalid credentials"}

from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend

@api.post("/signup")
def signup_view(request, username: str , email: str , password: str ):
    try:
        # Check if a user with the given username already exists
        if User.objects.filter(username=username).exists():
            return {"success": False, "message": "Username already exists"}

        # Create a new user
        user = User.objects.create_user(username, email, password)
        user.backend = 'allauth.account.auth_backends.AuthenticationBackend'

        login(request, user)
        return {"success": True}
    except IntegrityError:
        return {"success": False, "message": "Username or email already exists"}



@api.post("/logout")
def logout_view(request):
    logout(request)
    return {"success": True}
