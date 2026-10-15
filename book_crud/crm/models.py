from django.db import models
#book[id,title,author,price,pages,publications]
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    publication = models.CharField(max_length=200)