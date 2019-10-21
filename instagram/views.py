from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Foto,Comment,Follower,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,PostForm
from django.contrib import messages


@login_required(login_url='/accounts/login/')
def page(request):
    fotos = Foto.objects.all()
    return render(request,'all-posts/index.html',{"fotos":fotos})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('ownerprofile')
    else:
        form =ProfileForm
    return render(request, 'all-posts/profile.html', {"form": form})       

@login_required(login_url='/accounts/login/')
def ownerprofile(request,id):
    current_user = request.user
    user = Foto.objects.all()
    ifoto = Foto.objects.profile_by_id(id=id)
    return render(request, 'all-posts/owner.html', {"user": user,"usere":usere,"ifoto":ifoto,"current_user":current_user})       

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= current_user
            post.save()
        return redirect('page')
    else:
        form =PostForm
    return render(request, 'all-posts/post.html', {"form": form})
