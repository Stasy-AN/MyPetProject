from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('account/',views.account, name='account'),
    path('contakt/',views.contakt, name='contakt'),
    path('cats/',views.cats, name='cats'),
    path('sidebar/', views.sidebar),
]