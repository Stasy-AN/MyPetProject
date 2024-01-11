from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.utils import translation
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection, reset_queries
from django.views.decorators.csrf import csrf_exempt


from news.models import Article


def index (request):
    all_news = Article.objects.all().values('author','title')
    article = Article.objects.all().last()
    context = {'articles': all_news, 'article': article}

    return render(request, 'main/index.html', context)


def news(request):
    return render(request, 'main/news.html')

def list(request):
    return render(request, 'main/list.html')

def account(request):
    return render(request, 'main/account.html')


def contakt(request):
    return render(request, 'main/contakt.html')

def cats(request):
    return render(request, 'main/cats.html')



def custom_404(request, exception):
    #return render(request, 'main/sidebar.html')
    return HttpResponse('Котики работают над этим: {exception}')

def sidebar(request):
    return render(request,'main/sidebar.html')