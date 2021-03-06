from django.conf.urls import url

from . import views
from django.contrib.auth import views as loginviews

urlpatterns = [
	url(r'^$', loginviews.login,name="login"),
	url(r'^accounts/profile/$', views.redirecting,name="redirecting"),
	url(r'^logout/$', loginviews.logout, name="logout", kwargs={'next_page': '/'}),
	url(r'^car/add/$',views.add,name="add"),
	url(r'^manufacturer/add/$',views.add,name="add"),
	url(r'^person/add/$',views.add,name="add"),
	url(r'^car/(?P<pk>\d+)/$',views.displaylist,name="displaylist1"),
	url(r'^manufacturer/(?P<pk>\d+)/$',views.displaylist,name="displaylist2"),
	url(r'^person/(?P<pk>\d+)/$',views.displaylist,name="displaylist3"),
	url(r'^car/(?P<pk>\d+)/edit/$',views.edit,name="edit"),
	url(r'^manufacturer/(?P<pk>\d+)/edit/$',views.edit,name="edit"),
	url(r'^person/(?P<pk>\d+)/edit/$',views.edit,name="edit"),
	url(r'^car/$',views.viewCar, name="viewCar"),
	url(r'^manufacturer/$',views.viewManufacturer,name="viewManufacturer"),
	url(r'^person/$',views.viewPerson,name="viewPerson"),
	url(r'^car/(?P<pk>\d+)/delete/', views.delete, name="delete"),
	url(r'^manufacturer/(?P<pk>\d+)/delete/', views.delete, name="delete"),
	url(r'^person/(?P<pk>\d+)/delete/', views.delete, name="delete"),
]