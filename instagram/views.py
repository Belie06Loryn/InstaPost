from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def page(request):
    return render(request,'all-posts/index.html',)
