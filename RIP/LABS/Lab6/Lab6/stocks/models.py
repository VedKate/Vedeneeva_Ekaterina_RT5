from django.db import models

class Streets(models.Model): # Класс для таблицы streets
    idStreet=models.IntegerField(primary_key=True)
    StreetName = models.CharField(max_length=45)
    City = models.CharField(max_length=45)
     
    class Meta:  
        managed = False # при таком значении параметра подключится уже готовая таблица
        db_table = 'streets1'
