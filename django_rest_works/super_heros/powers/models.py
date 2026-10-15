from django.db import models

# Create your models here.

class SuperHeros(models.Model):

    name = models.CharField(max_length=200)

    POWER_OPTIONS = (
        ("fly", "Fly"),
        ("superspeed", "Superspeed"),
        ("superstrength", "Superstrength"),
        ("invisibility","Invisibility"),
        ("webshot","Webshot"),
        ("telepathy","Telepathy"),
        ("teleportation","Teleportation"),
        ("other","Other")

    )

    powers = models.CharField(max_length=200,choices=POWER_OPTIONS,default="other")

    category = models.CharField(max_length=200)

    weakness = models.CharField(max_length=200)

    universe = models.CharField(max_length=200)

    