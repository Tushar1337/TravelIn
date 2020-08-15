from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:myid>', views.post,name="post"),
    ]
