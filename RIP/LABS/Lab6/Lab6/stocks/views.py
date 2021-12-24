from django.shortcuts import render
from rest_framework import viewsets
from stocks.serializers import StockSerializer
from stocks.models import Streets


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Streets.objects.all()
    serializer_class = StockSerializer  # Сериализатор для модели
# Create your views here.
