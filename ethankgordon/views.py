from django.shortcuts import render


def index(request):
    current = 'home'
    return render(request, 'index.html', locals())

def projects(request):
    current = 'projects'
    return render(request, 'projects.html', locals())
