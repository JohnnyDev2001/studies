from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request, 'core/list.html', context={'name': 'Johnny'})

def index(request):
    return render(request, 'index.html')
