# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Manufacturer(models.Model):
	name = models.CharField(max_length=60)
	location = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Person(models.Model):
	firstname = models.CharField(max_length=60)
	lastname = models.CharField(max_length=60)

	def __str__(self):
		return "%s %s"%(self.firstname,self.lastname)

class Car(models.Model):
	carbrand = models.CharField(max_length = 60)
	carmodel = models.CharField(max_length = 60)
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	bought_by = models.ForeignKey(Person, on_delete=models.CASCADE)

	def __str__(self):
		return self.carbrand