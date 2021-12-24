
from RKapp.models import Streets
from RKapp.models import Houses
from rest_framework import serializers


class StreetsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Streets
        # Поля, которые мы сериализуем
        fields = ["idStreet", "StreetName", "City"]

class HousesSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Houses
        # Поля, которые мы сериализуем
        fields = ["idHouse", "num", "residents", "street_id"]