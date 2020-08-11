from django.db import models
from django.contrib.auth.models import User,auth
from django import forms
from django.conf import settings

class Destination(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField(max_length=200)
    price=models.IntegerField()
    pack= models.CharField(max_length=50)
    desc1 = models.TextField(max_length=200,null=True)

    def __str__(self):
        return self.name
class SpecialOffer(models.Model):
    name=models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    pack = models.CharField(max_length=50)
    offer=models.BooleanField(default=False)
    discount=models.IntegerField()

    day_1 = models.TextField(max_length=200, null=True, blank=True)
    day_1_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_2 = models.TextField(max_length=200, null=True, blank=True)
    day_2_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_3 = models.TextField(max_length=200, null=True, blank=True)
    day_3_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_4 = models.TextField(max_length=200, null=True, blank=True)
    day_4_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_5 = models.TextField(max_length=200, null=True, blank=True)
    day_5_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_6 = models.TextField(max_length=200, null=True, blank=True)
    day_6_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_7 = models.TextField(max_length=200, null=True, blank=True)
    day_7_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_8 = models.TextField(max_length=200, null=True, blank=True)
    day_8_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_9 = models.TextField(max_length=200, null=True, blank=True)
    day_9_img = models.ImageField(upload_to='pics', null=True, blank=True)

    day_10 = models.TextField(max_length=200, null=True, blank=True)
    day_10_img = models.ImageField(upload_to='pics', null=True, blank=True)


    def __str__(self):
        return self.name





class Packages(models.Model):
    name=models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    highlight = models.CharField(max_length=100, null=True)
    highlight1 = models.CharField(max_length=100, null=True)
    highlight2 = models.CharField(max_length=100, null=True)
    highlight3 = models.CharField(max_length=100, null=True)

    day_1=models.TextField(max_length=200,null=True,blank=True)
    day_1_img = models.ImageField(upload_to='pics',null=True,blank=True)

    day_2=models.TextField(max_length=200,null=True,blank=True)
    day_2_img = models.ImageField(upload_to='pics',null=True,blank=True)

    day_3=models.TextField(max_length=200,null=True,blank=True)
    day_3_img = models.ImageField(upload_to='pics',null=True,blank=True)

    day_4=models.TextField(max_length=200,null=True,blank=True)
    day_4_img = models.ImageField(upload_to='pics',null=True,blank=True)


    day_5=models.TextField(max_length=200,null=True,blank=True)
    day_5_img = models.ImageField(upload_to='pics',null=True,blank=True)


    day_6=models.TextField(max_length=200,null=True,blank=True)
    day_6_img = models.ImageField(upload_to='pics',null=True,blank=True)


    day_7=models.TextField(max_length=200,null=True,blank=True)
    day_7_img = models.ImageField(upload_to='pics',null=True,blank=True)


    day_8=models.TextField(max_length=200,null=True,blank=True)
    day_8_img = models.ImageField(upload_to='pics',null=True,blank=True)


    day_9=models.TextField(max_length=200,null=True,blank=True)
    day_9_img = models.ImageField(upload_to='pics',null=True,blank=True)


    day_10=models.TextField(max_length=200,null=True,blank=True)
    day_10_img = models.ImageField(upload_to='pics',null=True,blank=True)

    def __str__(self):
        return self.name




class Reviews(models.Model):
    reviewer_img=models.ImageField(upload_to='pics', null=True,blank=True,default='testimonial1.jpg')
    review=models.TextField(max_length=200, null=True, blank=True)
    review_name=models.CharField(max_length=50, null=True, blank=True)
    address=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.review_name






class Contact(models.Model):
    name=models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    package=models.CharField(max_length=100, null=True)
    message= models.TextField(max_length=1000)



    def __str__(self):
        return self.name







