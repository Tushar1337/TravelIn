from django.shortcuts import render
from django.apps import apps
post2=apps.get_model('blog', 'post')


def post(request,myid):
    post1=post2.objects.filter(id=myid)
    return render(request, "post.html", {"posts": post1[0]})
