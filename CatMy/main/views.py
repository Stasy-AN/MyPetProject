from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def list(request):
    return render(request, 'main/list.html')

def account(request):
    return render(request, 'main/account.html')

def news2(request):
    return render(request, 'main/news2.html')

def contakt(request):
    return render(request, 'main/contakt.html')

def cats(request):
    return render(request, 'main/cats.html')