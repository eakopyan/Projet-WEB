from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime 
from blog.models import User, Event
from .forms import SignInForm

# Create your views here.

def home(request):
	
	user = User.objects.all()
	return render(request, 'blog/accueil.html', {'liste_user':user})


#affiche la page d'accueil d'un user précis
def user(request,id,slug):
	utilisateur=get_object_or_404(User, id=id, slug=slug)
	
	return render(request, 'blog/user.html', {'user':utilisateur})


#affiche le formulaire SignIn
def signIn(request):
	form = SignInForm(request.POST or None)
	user = User()
	if form.is_valid():
		user.username = form.cleaned_data['username']
		user.password = form.cleaned_data['password']
		user.save()
		envoi = True
	
	return render(request, 'blog/form.html', locals())


