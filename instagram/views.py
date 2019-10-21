from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Foto,Comment,Follower,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,PostForm,CommentForm
from django.contrib import messages


@login_required(login_url='/accounts/login/')
def page(request):
    fotos = Foto.objects.all()
    form = CommentForm()
    profile = Profile.objects.all()
    return render(request,'all-posts/index.html',{"fotos":fotos,"form":form,"profile":profile})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid() and upform.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('ownerprofile')
    else:
        form =ProfileForm(instance=request.user)
    return render(request, 'all-posts/profile.html', {"form": form})       

@login_required(login_url='/accounts/login/')
def ownerprofile(request,user=None):
    current_user = request.user
    ifoto = Foto.objects.all()
    profile = Profile.objects.all()
    foto = Foto.objects.filter(profile=current_user)
    if not user:
        user = request.user
        ifotos = Foto.objects.filter(name=user)
    return render(request, 'all-posts/owner.html',locals(),{"profile":profile,"foto":foto,"ifoto":ifoto,"current_user":current_user})       

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

def search_results(request):
    if 'usere' in request.GET and request.GET['usere']:
        search = request.GET.get("usere")
        searched = Profile.find_profile(search)
        user = Profile.objects.all()
        
        return render(request, 'all-posts/search.html',{"user":user,"usere":searched})   

@login_required
def Comment(request,pk):
    current_user = request.user
    image = Foto.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image = image
            comment.save()
            return redirect(Index)
    else:       
        return redirect(Index)
