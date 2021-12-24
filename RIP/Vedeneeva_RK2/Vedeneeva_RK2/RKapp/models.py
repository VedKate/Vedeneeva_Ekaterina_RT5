# models.py
from django.db import models

class Streets(models.Model): # Класс для таблицы streets
    idStreet=models.IntegerField(primary_key=True)
    StreetName = models.CharField(max_length=45)
    City = models.CharField(max_length=45)
     
    class Meta:  
        managed = False # при таком значении параметра подключится уже готовая таблица
        db_table = 'streets'

class Houses(models.Model):
    idHouse = models.IntegerField(primary_key=True)
    num = models.IntegerField()
    residents = models.CharField(max_length=45)
    street = models.ForeignKey(Streets, models.DO_NOTHING) # задаем внешний ключ

    class Meta:
        managed = False
        db_table = 'houses'

