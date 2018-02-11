# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CarForm,ManufacturerForm,PersonForm
from .filters import CarFilter,ManufacturerFilter,PersonFilter
from .models import Car
from .models import Manufacturer
from .models import Person

# Create your views here.

@login_required(login_url='/')
def viewCar(request):
	carlist = Car.objects.all()
	carfilter = CarFilter(request.GET, queryset=carlist)
	return render(request, 'mylists/viewCar.html',{'filter':carfilter})

@login_required(login_url='/')
def viewManufacturer(request):
	manufacturerlist = Manufacturer.objects.all()
	manufacturerfilter = ManufacturerFilter(request.GET, queryset=manufacturerlist)
	return render(request, 'mylists/viewManufacturer.html',{'filter':manufacturerfilter})

@login_required(login_url='/')
def viewPerson(request):
	personlist = Person.objects.all()
	personfilter = PersonFilter(request.GET, queryset=personlist)
	return render(request, 'mylists/viewPerson.html',{'filter':personfilter})

@login_required(login_url='/')
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

	elif "manufacturer" in request.META.get("HTTP_REFERER"):
		if request.method == "POST":
			form = ManufacturerForm(request.POST)
			if form.is_valid():
				manufacturer = form.save()
				manufacturer.save()
				return redirect('viewManufacturer')
		else:
			form = ManufacturerForm()
			return render(request, 'mylists/add.html', {'form':form})
	
	elif "person" in request.META.get("HTTP_REFERER"):
		if request.method == "POST":
			form = PersonForm(request.POST)
			if form.is_valid():
				person = form.save()
				person.save()
				return redirect('viewPerson')
		else:
			form = PersonForm()
			return render(request, 'mylists/add.html', {'form':form})

@login_required(login_url='/')
def displaylist(request, pk):
	if "car" in request.META.get("HTTP_REFERER"):
		car = get_object_or_404(Car, pk=pk)
		return render(request, 'mylists/displaylist.html', {'car':car})
	elif "manufacturer" in request.META.get("HTTP_REFERER"):
		manufacturer = get_object_or_404(Manufacturer, pk=pk)
		return render(request, 'mylists/displaylist.html', {'manufacturer':manufacturer})
	elif "person" in request.META.get("HTTP_REFERER"):
		person = get_object_or_404(Person, pk=pk)
		return render(request, 'mylists/displaylist.html', {'person':person})

@login_required(login_url='/')
def edit(request,pk):
	if "car" in request.META.get("HTTP_REFERER"):
		car = get_object_or_404(Car,pk=pk)
		if request.method == "POST":
			form = CarForm(request.POST, instance=car)
			if form.is_valid():
				car=form.save()
				car.save()
				return redirect('viewCar')
		else:
			form = CarForm(instance=car)
			return render(request,'mylists/add.html',{'form':form})
	
	elif "manufacturer" in request.META.get("HTTP_REFERER"):
		manufacturer = get_object_or_404(Manufacturer,pk=pk)
		if request.method == "POST":
			form = ManufacturerForm(request.POST, instance=manufacturer)
			if form.is_valid():
				manufacturer=form.save()
				manufacturer.save()
				return redirect('viewManufacturer')
		else:
			form = ManufacturerForm(instance=manufacturer)
			return render(request,'mylists/add.html',{'form':form})

	elif "person" in request.META.get("HTTP_REFERER"):
		person = get_object_or_404(Person,pk=pk)
		if request.method == "POST":
			form = PersonForm(request.POST, instance=person)
			if form.is_valid():
				person=form.save()
				person.save()
				return redirect('viewPerson')
		else:
			form = PersonForm(instance=person)
			return render(request,'mylists/add.html',{'form':form})

@login_required(login_url='/')
def delete(request,pk):
	if "car" in request.META.get("HTTP_REFERER"):
		car = get_object_or_404(Car,pk=pk)
		car.delete()
		return redirect('viewCar')
	elif "manufacturer" in request.META.get("HTTP_REFERER"):
		manufacturer = get_object_or_404(Manufacturer,pk=pk)
		manufacturer.delete()
		return redirect('viewManufacturer')
	elif "person" in request.META.get("HTTP_REFERER"):
		person = get_object_or_404(Person,pk=pk)
		person.delete()
		return redirect('viewPerson')

def redirecting(request):
	return redirect('viewCar')