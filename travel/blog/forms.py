from django import forms
from django.apps import apps
from .views import *
from .models import comments

Contact = apps.get_model('website', 'Contact')


class contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'mobile', 'package','message')
class comment(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('post','comments','name')
        widgets = {'post': forms.HiddenInput(),'name': forms.HiddenInput()}