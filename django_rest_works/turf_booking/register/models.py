from django.db import models
from booking.models import TurfBook
# Create your models here.


class Booking(models.Model):
    
    team_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=200)

    email = models.EmailField()

    turf = models.ForeignKey(TurfBook,on_delete=models.CASCADE)

    date = models.DateField()

    time = models.TimeField()

    duration = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name