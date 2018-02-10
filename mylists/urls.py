from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^car/add/$',views.add,name="add"),
	url(r'^manufacturer/add/$',views.add,name="add"),
	url(r'^person/add/$',views.add,name="add"),
	url(r'^car/$',views.viewCar, name="viewCar"),
	url(r'^manufacturer/$',views.viewManufacturer,name="viewManufacturer"),
	url(r'^person/$',views.viewPerson,name="viewPerson"),
]