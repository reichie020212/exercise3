from django import forms
from .models import Car, Person, Manufacturer

class CarForm(forms.ModelForm):

	class Meta:
		model = Car
		fields = {'carbrand','bought_by','manufacturer','carmodel',}

class PersonForm(forms.ModelForm):

	class Meta:
		model = Person
		fields = {'lastname','firstname',}

class ManufacturerForm(forms.ModelForm):

	class Meta:
		model = Manufacturer
		fields = {'name','location',}