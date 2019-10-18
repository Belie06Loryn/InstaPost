from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Foto,Comment,Follower,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required(login_url='/accounts/login/')
def page(request):
    return render(request,'all-posts/index.html',)

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save_profile(commit=False)
            profile.username = current_user
            profile.save_profile()
        return redirect('owner')

    else:
        form = ProfileForm()
    return render(request, 'all-posts/profile.html', {"form": form})       