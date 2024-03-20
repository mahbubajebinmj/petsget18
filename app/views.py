from profile import Profile
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from .utils import *
from django.contrib.auth import User
from .models import *
import uuid 

def index(request):
    return render(request, "index.html" )

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User(username = email)
        user_obj.set_password(password)
        p_obj = Profile.objects.create(
            user = user_obj,
            email_token = str(uuid.uuid4())
        )
        send_email_token(email, p_obj.email_token)
    return render(request, "login.html" )


