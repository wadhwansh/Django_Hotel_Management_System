from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import *

def about(request):
    return render(request,"about.html")
def hello(request):
    return HttpResponse("Hello guyzs!! my name is Ansh wadhwa.")
def name1(request,age):
    return HttpResponse(age) 
def first(request):
    return render(request,"first.html")
def index(request):
    return render(request,"index.html")
def booking(request):
    return render(request,"booking.html")
def gallary(request):
    return render(request,"gallery.html")
def review(request):
    if request.method == "POST":
        data=request.POST
        Name=data.get('Name')
        Email=data.get('Email')
        Phone=data.get('Phone')
        Review=data.get('Review')
        feedback.objects.create(
            Name=Name,
            Email=Email,
            Phone=Phone,
            Review=Review,
        )
        redirect('reviews.html')
    return render(request,"reviews.html")
   
def room(request):
    return render(request,"rooms.html")
def services(request):
    return render(request,"services.html")
