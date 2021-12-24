from django.shortcuts import render
from rest_framework import viewsets
from RKapp.serializers import StreetsSerializer
from RKapp.serializers import HousesSerializer
from RKapp.models import Streets, Houses 


class StreetsSet(viewsets.ModelViewSet):
    queryset = Streets.objects.all()
    serializer_class =  StreetsSerializer # Сериализатор для модели

class HousesSet(viewsets.ModelViewSet):
    queryset = Houses.objects.all()
    serializer_class =  HousesSerializer # Сериализатор для модели

def report(request):
    return render (request, 'rep.html' , {'data':{
        'houses': Houses.objects.select_related('street')
        }})