from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class post(models.Model):
    post_img=models.ImageField(upload_to='pics')
    category = models.CharField(max_length=50,null=True)
    Title=models.CharField(max_length=100)
    desc=models.TextField(max_length=1000)
    post_sub_img=models.ImageField(upload_to='pics')
    sub_head=models.CharField(max_length=100)
    sub_desc = models.TextField(max_length=1000)
    author = models.CharField(max_length=50,null=True)
    date = models.DateTimeField(default=datetime.now)

class comments(models.Model):
    post=models.ForeignKey(post, on_delete=models.SET_NULL,null=True)
    comments = models.CharField(max_length=1000)
    name = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now)

