from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination,SpecialOffer,Packages
def index(request):


    dest=Destination.objects.all()
    offer=SpecialOffer.objects.all()
    package=Packages.objects.all()

    return render(request,'index.html',{'dests':dest,'offers':offer,'packages':package})
