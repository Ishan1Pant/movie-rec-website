from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('find',views.find,name='find'),
    path('contact',views.contact_us,name='contact'),
]