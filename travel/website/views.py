from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
from .models import Destination,SpecialOffer,Packages,Reviews
post2=apps.get_model('blog', 'post')
def index(request):


    dest=Destination.objects.all()
    offer=SpecialOffer.objects.all()
    package=Packages.objects.all()
    review=Reviews.objects.all()
    post1 = post2.objects.all().reverse()[::-1]
    print(post1)

    return render(request,'index.html',{'dests':dest,'offers':offer,'packages':package,'reviews':review,"posts": post1[:5]})
