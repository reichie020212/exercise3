# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Person, Car, Manufacturer

# Create your views here.

def viewCar(request):
	car = Car.objects.all()
	render(request, 'mylists/viewCar.html',{'car':car})

def viewManufacturer(request):
	manufacturer = Manufacturer.objects.all()
	render(request,'mylists/viewManufacturer.html',{'manufacturer':manufacturer})

def viewPerson(request):
	person = Person.objects.all()
	render(request,'mylists/viewPerson.html',{'person':person})

