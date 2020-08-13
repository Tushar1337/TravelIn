from django import forms
from django.apps import apps
from .views import *

Contact = apps.get_model('website', 'Contact')


class contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'mobile', 'package','message')
