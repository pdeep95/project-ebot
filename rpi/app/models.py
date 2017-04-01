from django.db import models

# Create your models here.

class Process(models.Model):
    pid = models.IntegerField()
    direction = models.CharField(max_length=128, default='None')
    def __str__(self):
        return str(self.pid)