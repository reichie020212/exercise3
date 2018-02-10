# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import redirect, get_object_or_404

from .forms import CarForm,ManufacturerForm,PersonForm
from .models import Car
from .models import Manufacturer
from .models import Person

# Create your views here.

def viewCar(request):
	car = Car.objects.all()
	return render(request, 'mylists/viewCar.html',{'car':car})

def viewManufacturer(request):
	manufacturer = Manufacturer.objects.all()
	return render(request,'mylists/viewManufacturer.html',{'manufacturer':manufacturer})

def viewPerson(request):
	person = Person.objects.all()
	return render(request,'mylists/viewPerson.html',{'person':person})

def add(request):
	if "car" in request.META.get("HTTP_REFERER"):
		if request.method == "POST":
			form = CarForm(request.POST)
			if form.is_valid():
				car = form.save()
				car.save()
				return redirect('viewCar')
		else:
			form = CarForm()
			return render(request, 'mylists/add.html', {'form':form})

	if "manufacturer" in request.META.get("HTTP_REFERER"):
		if request.method == "POST":
			form = ManufacturerForm(request.POST)
			if form.is_valid():
				manufacturer = form.save()
				manufacturer.save()
				return redirect('viewManufacturer')
		else:
			form = ManufacturerForm()
			return render(request, 'mylists/add.html', {'form':form})
	
	if "person" in request.META.get("HTTP_REFERER"):
		if request.method == "POST":
			form = PersonForm(request.POST)
			if form.is_valid():
				person = form.save()
				person.save()
				return redirect('viewPerson')
		else:
			form = PersonForm()
			return render(request, 'mylists/add.html', {'form':form})
