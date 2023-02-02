from django.urls import path
from . import views

urlpatterns = [

    path('', views.landingpage, name='homepage'),
    path('list', views.listpage, name='listpage'),
    path('/check_email', views.check_email, name='checkmail')

]