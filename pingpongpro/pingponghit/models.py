from django.db import models

# Create your models here.
class Pingponghit(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField()
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.title