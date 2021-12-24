from stocks.models import Streets
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Streets
        # Поля, которые мы сериализуем
        fields = ["idStreet", "StreetName", "City"]
