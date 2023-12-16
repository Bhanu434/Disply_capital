from django.db import models

# Create your models here.
class Country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.country_name
class Capital(models.Model):
    country_name=models.OneToOneField(Country,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.city_name
