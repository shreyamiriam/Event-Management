from django.shortcuts import render,redirect
from .models import Event
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')
def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    forms=BookingForm()
    dict_form={
        'form1':forms

    }
    return render(request,'Booking.html',dict_form)
def contact(request):
    return render(request,'Contact.html')
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'Events.html',dict_eve)
