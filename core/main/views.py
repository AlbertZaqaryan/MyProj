from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('index')
    return render(request, 'main/index.html', context={

    })