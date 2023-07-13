from django.shortcuts import render


# Create your views here.

def index (request):
    return render(request,"index.html")
def home (request):
    return render(request,"home.html")

def about (request):
    return render(request,"about.html")

def services (request):
    return render(request,"services.html")

def helpline (request):
    return render(request,"help-line.html")

def contact (request):
    return render(request,"contact.html")

def signin (request):
    return render(request,"sign-in.html")

def register (request):
    return render(request,"register.html")