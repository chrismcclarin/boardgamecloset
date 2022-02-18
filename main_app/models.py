from django.db import models
from django.urls import reverse


class SaleLocation(models.Model):
    date = models.DateField()
    store = models.CharField(max_length=100)
    salevalue = models.IntegerField()

    def __str__(self):
        return f"{self.store} is having a {self.salevalue} percent off sale on {self.date}"

    def get_absolute_url(self):
        return reverse('sale_detail', kwargs={'sale_id': self.id})

class Games(models.Model):
    name= models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    preferredplayers=models.IntegerField()
    timetoplay=models.IntegerField()
    description=models.TextField(max_length=250)
    sale = models.ManyToManyField(SaleLocation)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

class GameTime(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    timeplayed = models.IntegerField()

    game = models.ForeignKey(Games, on_delete=models.CASCADE)
