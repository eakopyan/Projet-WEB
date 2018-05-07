from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length = 20)

	class Meta:
		verbose_name="utilisateur"
		ordering=['username'] #trier par nom d'user

	def __str__(self):
		""""
		Aucune idée de ce que c'est cette merde, mais ça beug sinon"""
		return self.username
	
class Event(models.Model):
	name = models.CharField(max_length=100)
	descritption = models.TextField(null=True) #pas de limite 
	date = models.DateTimeField(default=timezone.now, verbose_name= "Date de l'evenement")

	class Meta: 
		verbose_name="evenement"
		ordering = ['date'] #trier par date 

	def __str__(self):
		""""
		Aucune idée de ce que c'est cette merde, mais ça beug sinon"""
		return self.name

