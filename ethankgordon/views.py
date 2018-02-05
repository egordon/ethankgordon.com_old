from django.shortcuts import render
from blog.models import Article


def index(request):
    current = 'home'
    recentArticle = Article.objects.latest('created')
    return render(request, 'index.html', locals())

def contact(request):
    current = 'contact'
    return render(request, 'contact.html', locals())

def projects(request):
    current = 'projects'
    return render(request, 'projects.html', locals())

def keybase(request):
    current = 'keybase'
    return render(request, 'keybase.txt', locals())
