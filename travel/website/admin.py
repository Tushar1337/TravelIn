from django.contrib import admin
from django.apps import apps
from .models import Destination,SpecialOffer,Packages,Reviews,Contact
post=apps.get_model('blog', 'post')
admin.site.register(Destination)
admin.site.register(SpecialOffer)
admin.site.register(Packages)
admin.site.register(Reviews)
admin.site.register(Contact)
admin.site.register(post)