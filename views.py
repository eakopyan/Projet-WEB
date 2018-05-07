from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime 
from blog.models import User, Event
# Create your views here.
def home(request):
	"""Welcome to realivent ! Mettez-nous 20 svp. Voici la liste de nos utilisateurs """
	user = User.objects.all()
	return render(request, 'blog/accueil.html', {'liste_user':user})


def view_user(request, id):
	if id > 100 :
		return redirect(view_redirection)
	else :
		return render(request, 'blog/user.html', {'id':id})
		

def view_redirection(request):
	return HttpResponse("Vous avez été redirigé")

def date_actuelle(request):
	return render(request, 'blog/date.html', {'date':datetime.now()})


