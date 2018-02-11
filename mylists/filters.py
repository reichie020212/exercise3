import django_filters
from .models import Car,Manufacturer,Person

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['carbrand', 'carmodel', 'manufacturer','bought_by', ]

class ManufacturerFilter(django_filters.FilterSet):
    class Meta:
        model = Manufacturer
        fields = ['name', 'location',]

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname',]