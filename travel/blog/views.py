from django.shortcuts import render,redirect
from django.apps import apps
from .forms import comment

post2=apps.get_model('blog', 'post')
comments=apps.get_model('blog', 'comments')

def post(request,myid):
    post1=post2.objects.filter(id=myid)
    comment1=comments.objects.filter(post=post1[0])
    current_user = request.user
    if request.method == 'POST':
        form = comment(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("valid")
            form.save()
    form=comment(initial={ 'post':post1[0] ,'comments': '','name':current_user.first_name})




    print(comment)
    return render(request, "post.html", {"posts": post1[0],'comments':comment1,'form':form,'user':current_user})
