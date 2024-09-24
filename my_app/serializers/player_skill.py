from rest_framework import serializers 

from ..models.player_skill import PlayerSkill

class PlayerSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerSkill
        fields = ['id', 'skill', 'value', 'player_id']
        extra_kwargs = {"skill": {"error_messages": {'blank': 'Skill cannot be blank', 'required': 'Skill is required'}}, "value": {"error_messages": {'blank': 'Value cannot be blank', 'required': 'Value is required'}}}


class PlayerSkillForTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerSkill
        fields = ['skill', 'value']
        extra_kwargs = {"skill": {"error_messages": {'blank': 'Skill cannot be blank', 'required': 'Skill is required'}}, "value": {"error_messages": {'blank': 'Value cannot be blank', 'required': 'Value is required'}}}

