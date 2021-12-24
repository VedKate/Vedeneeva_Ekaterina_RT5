from django.shortcuts import render
from lab5.models import Streets
from lab5.models import Houses
from datetime import date


def streetList(request): #открытие стартовой страницы 
    return render(request, 'lab5\\streets.html', {'data' : {
        'current_date': date.today(),
        'streets': Streets.objects.all()
           }})


def GetStreet(request, id): # открытие страницы для конкретной улицы
    return render(request, 'lab5\\houses.html', {'data':{
         'current_date': date.today(),
         'houses': Houses.objects.filter(street=id), # запрос на дома, находящиеся на данной улице
        }})