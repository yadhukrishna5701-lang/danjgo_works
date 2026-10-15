from django.db import models

# Create your models here.

class TurfBook(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.PositiveIntegerField()
    fee = models.PositiveIntegerField()

    def __str__(self):

        return self.name
