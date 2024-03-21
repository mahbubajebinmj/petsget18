from profile import Profile
from django.http import HttpResponse
from django.shortcuts import render
<<<<<<< HEAD

#from django.contrib.auth import User
from .models import *

from django.core.mail import send_mail
from petsget.settings import EMAIL_HOST_USER
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


=======
from django.shortcuts import render
from .utils import *
from django.contrib.auth import User
from .models import *
import uuid 
>>>>>>> 1baf8065ac4f3616ce0644d08045d47b515619ff


def login(request):
<<<<<<< HEAD
    #subject = request.POST.get("subject", "")
    #message = request.POST.get("message", "")
    from_email = request.POST.get('email',"from_email", "")
    if request.method == "POST":
        email = request.POST.get('email')
        send_mail( EMAIL_HOST_USER, [email])
        return render(request, 'verify.html')
        

'''def index(request):
    send_mail(
    "nije code kore code dekho",
    "kisher eto code dekhte chao tumi??",
    "petsget.online@gmail.com",
    ["taranaislam20@gmail.com"],
    fail_silently=False,
)
    return render(request, "index.html" )
'''
    
    
    
    
    
    
    
    
    
    
=======
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


>>>>>>> 1baf8065ac4f3616ce0644d08045d47b515619ff
