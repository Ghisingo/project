from django.shortcuts import render

from website

# Create your views here.

def index(request):
    return render(request, 'website/index.html')
