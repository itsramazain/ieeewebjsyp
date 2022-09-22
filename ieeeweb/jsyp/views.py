from django.shortcuts import render

# Create your views here.

def soon(request):
    return render(request,'jsyp/soon.html')

def home(request):
    return render(request,'jsyp/home.html')


def aboutus(request):
    return render(request,'jsyp/aboutus.html')



def congresscom(request):
    return render(request,'jsyp/congresscom.html')



def contactus(request):
    return render(request,'jsyp/contactus.html')


def embassidor(request):
    return render(request,'jsyp/embassidor.html')


def ieee(request):
    return render(request,'jsyp/ieee.html')



def ieeehusb(request):
    return render(request,'jsyp/ieeehusb.html')



def ieeeypafg(request):
    return render(request,'jsyp/ieeeypafg.html')


def keynotespeech(request):
    return render(request,'jsyp/keynotespeech.html')



def oandecom(request):
    return render(request,'jsyp/oandecom.html')



def regester(request):
    return render(request,'jsyp/regester.html')



def speakers(request):
    return render(request,'jsyp/speakers.html')



def steering(request):
    return render(request,'jsyp/steering.html')



def volunteers(request):
    return render(request,'jsyp/volunteers.html')



def wrkshops(request):
    return render(request,'jsyp/workshops.html')
