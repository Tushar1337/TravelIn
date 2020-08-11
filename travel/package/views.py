from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.apps import apps
from .forms import contact


Packages=apps.get_model('website', 'Packages')




def packview(request,myid):
    package=Packages.objects.filter(id=myid)
    current_user = request.user
    a = current_user.first_name


    if request.method == 'POST':
        form = contact(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("valid")
            form.save()
    form=contact(initial={'name':current_user.first_name,'package':Packages.objects.get(pk=myid) ,'message': 'Hi'})
    return render(request, "packageview.html", {"packages": package[0],'form':form})


