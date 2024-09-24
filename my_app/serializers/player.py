from rest_framework import serializers 

from .player_skill import PlayerSkillSerializer, PlayerSkillForTeamSerializer
from ..models.player import Player

class PlayerSerializer(serializers.ModelSerializer):
    playerSkills = PlayerSkillSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'playerSkills']
        extra_kwargs = {"name": {"error_messages": {'blank': 'Name cannot be blank', 'required': 'Name is required'}}, "name": {"error_messages": {'blank': 'Position cannot be blank', 'required': 'Position is required'}}}


class PlayerForTeamSerializer(serializers.ModelSerializer):
    playerSkills = PlayerSkillForTeamSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ['name', 'position', 'playerSkills']
