from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Foodlogs(models.Model):


    title = models.CharField(max_length=200)

    calories = models.IntegerField()

    MEAL_TYPE_CHOICES = [
        ("BREAKFAST","breakfast"),
        ("LUNCH","lunch"),
        ("DINNER","dinner"),
        ("SNACK","snack"),
    ]

    meal_type = models.CharField(
        max_length=200,
        choices=MEAL_TYPE_CHOICES
    )

    serving_size = models.CharField(max_length=100)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="foodlods"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"