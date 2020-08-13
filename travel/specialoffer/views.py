from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
from .forms import contact
Special_Offer=apps.get_model('website', 'SpecialOffer')


def special(request,myid):
    special=Special_Offer.objects.filter(id=myid)
    current_user = request.user
    a = current_user.first_name

    if request.method == 'POST':
        form = contact(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("valid")
            form.save()
    form = contact(initial={'name': current_user.first_name, 'package': Special_Offer.objects.get(pk=myid), 'message': 'Hi'})
    return render(request,"special.html",{"special":special[0],'form':form})