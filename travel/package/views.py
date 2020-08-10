from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
Packages=apps.get_model('website', 'Packages')
def packview(request,myid):
    package=Packages.objects.filter(id=myid)
    return render(request,"packageview.html",{"packages":package[0]})
