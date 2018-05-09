"""fichier URL de l'APPLICATION BLOG et non du projet !!! """

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('user/<int:id>', views.user, name='user'), 
	path('SignIn', views.signIn, name='signIn'),
	
]
