from django.http import HttpResponse
from django.shortcuts import render

#from django.contrib.auth import User
from .models import *

from django.core.mail import send_mail
from petsget.settings import EMAIL_HOST_USER
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect




def login(request):
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
    
    
    
    
    
    
    
    
    
    