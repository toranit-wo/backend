from django.db import models

# Create your models here.
class Pingponghit(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField()

class Totalhit(models.Model):
    title = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    hitHavg = models.IntegerField(default=0)
    hitCavg = models.IntegerField(default=0)
    hitLavg = models.IntegerField(default=0)
