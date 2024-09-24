
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=64, blank=False, default='')
    position = models.CharField(max_length=16, blank=False)
