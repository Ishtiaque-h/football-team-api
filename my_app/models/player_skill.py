from django.db import models

from .player import Player

class PlayerSkill(models.Model):
    player = models.ForeignKey(Player, related_name='playerSkills', on_delete=models.CASCADE)
    skill = models.CharField(max_length=16, blank=False)
    value = models.IntegerField()
