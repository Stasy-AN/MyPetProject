from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('news/',views.news, name='news'),
    path('list/',views.list, name='list'),
    path('account/',views.account, name='account'),
]