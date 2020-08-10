from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
Special_Offer=apps.get_model('website', 'SpecialOffer')
def special(request,myid):
    special=Special_Offer.objects.filter(id=myid)
    return render(request,"special.html",{"special":special[0]})