from django.shortcuts import render
from datetime import date


def hello(request):
    return render(request, 'index.html', {'data': {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def GetHouses(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Дом №1', 'id': 1},
            {'title': 'Дом №2', 'id': 2},
            {'title': 'Дом №3', 'id': 3},
        ]
    }})


def GetHouse(request, id):
    return render(request, 'order.html', {'data': {
        'current_date': date.today(),
        'id': id
    }})

# <a href="{% url 'order_url' order.id %}">{{ order.title }}</a>