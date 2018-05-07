"""fichier URL de l'APPLICATION BLOG et non du projet !!! """

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='accueil'),
	path('user/<int:id>', views.view_user), 
	path('redirection', views.view_redirection),
	path('date', views.date_actuelle),
]
