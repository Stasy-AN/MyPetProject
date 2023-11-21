from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('news/',views.news, name='news'),
    path('list/',views.list, name='list'),
    path('account/',views.account, name='account'),
    path('news2/',views.news2, name='news2'),
    path('contakt/',views.contakt, name='contakt'),
    path('cats/',views.cats, name='cats'),
]