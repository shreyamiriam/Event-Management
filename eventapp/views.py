from django.shortcuts import render
from .models import Event

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')
def booking(request):
    return render(request,'Booking.html')
def contact(request):
    return render(request,'Contact.html')
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'Events.html',dict_eve)
