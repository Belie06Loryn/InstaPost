from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Foto,Comment,Follower,Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def page(request):
    return render(request,'all-posts/index.html',)
