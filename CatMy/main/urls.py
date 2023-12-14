from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('news/', views.news, name='news'),
    path('account/',views.account, name='account'),
    path('contakt/',views.contakt, name='contakt'),
    path('cats/',views.cats, name='cats'),
    path('sidebar/', views.sidebar),
]