from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^car/$',views.viewCar, name="viewCar"),
	url(r'^manufacturer/$',views.viewManufacturer,name="viewManufacturer"),
	url(r'^person/$',views.viewPerson,name="viewPerson"),
]