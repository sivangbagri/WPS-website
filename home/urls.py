from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('teachers/', views.teachers, name='teachers'),
    path('events/', views.events, name='events'),
    path('fees/', views.fees, name='fees'),
    path('notice/', views.notice, name='notice'),
    path('myself/', views.myself, name='myself'),
    path('search/', views.search, name='search'),
    path('subject/', views.subject, name='subject'),
]
