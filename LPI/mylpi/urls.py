from unicodedata import name
from django.contrib import admin
from django.urls import path
from mylpi import views
# from python.LPI_code.Number_plate_detection import details

urlpatterns = [
   path('',views.home,name='home'),
   path('contact/',views.contact,name='contact'),
   path('work/',views.work,name='work'),
   path('client/',views.client,name='client'),
   path('about/',views.about,name='about'),
   path('singin/',views.singin,name='singin'),
   path('singup/',views.singup,name='singup')

]