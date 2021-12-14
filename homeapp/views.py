from os import name
from django.conf.urls import url
import json
from django.http import response
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from homeapp.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    context = {
        'variable1' : ' variable one',
        'variable2' : 'second variable.'
    }
    return render(request, 'index.html', context)
    # return HttpResponse(" this is home")

def about(request):
    # return HttpResponse(" this is about")
    return render (request, "about.html")

def contact(request):
    # return HttpResponse(" this is contact")
    if request.method == "POST":
        
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, number= number, email=email, desc= desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your enquiery form has been submitted!')

    
    return render(request, 'contact.html')

def services(request):
    # return HttpResponse(" this is services")
    return render(request, 'services.html')


def booKingfunction(request):
    # url="booKing"
    return render(request, 'booking.html')


@csrf_exempt
def room_type_list(request):
    
    data = Room.objects.values('id', 'room_no')
    print(data)
    room_dict= []
    for i in data:
        room_dict.append(i)
    response = JsonResponse({'status':'success', 'room_dict': room_dict})
    return response

def addbookingsapi(request):

    if request.method == "POST":

        Name = request.POST.get('Name')
        no = request.POST.get('no')
        email =request.POST.get('email')
        address = request.POST.get('address')
        room_type = request.POST.get('room_type')
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        
        newuser = Userprofile.objects.create(Name=Name, no=no, email=email, address=address)
        newuser.save()
        id= newuser.id
        print(id)
        print(room_type,'this is test')

        room = Room.objects.get(id=room_type)
        uid= Userprofile.objects.get(id = id)
        
        newbooking =BooKings.objects.create(user=uid, checkin_date= check_in, chekout_date= check_out, room_type=room )
        newbooking.save()
        messages.success(request, 'Thank you, Your Booking has been done!')



        # booKings.objects.create(checkin_date= check_in, chekout_date= check_out).save()       
        
        # try:
        #     room_type = request.POST.get('room_type')
        # except:
        #     room_type = 0
            

        

        

            