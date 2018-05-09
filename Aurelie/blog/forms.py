from django import forms
from django.utils import timezone

class SignInForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length =20)
	email = forms.EmailField(label = "Votre adresse mail")
	
class CreateEvent(forms.Form):	
	name = forms.CharField(max_length = 100)
	description = forms.CharField(widget = forms.Textarea)
	date = forms.DateField(widget =forms.DateInput)
	public = forms.BooleanField(help_text="Cochez si vous voulez que votre evenement soit public \n")

	
	
