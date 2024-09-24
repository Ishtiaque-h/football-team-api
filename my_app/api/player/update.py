from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from typing import Any
from django.db import transaction
from ...models.player import Player
from ...models.player_skill import PlayerSkill
from ...models.values import Constant
from ...serializers.player import PlayerSerializer
from ...serializers.player_skill import PlayerSkillSerializer


def get_serializer_error(the_serializer):
    for key, value in the_serializer.errors.items():
        return the_serializer.errors[key][0]
    return ""

@transaction.atomic
def update_player_handler(request: Request, id: Any):
    player_ = None
    try:
        player_ = Player.objects.get(pk=id)
    except Player.DoesNotExist:
        return JsonResponse({"message":"Player does not exist"}, status=status.HTTP_404_NOT_FOUND, safe=False)
    player_serializer = PlayerSerializer(player_, data=request.data, partial=True)
    if player_serializer.is_valid():
        position_ = player_serializer.validated_data["position"]
        if position_ not in Constant.positions:
            return JsonResponse({"message":f"Invalid value for position: {position_}"}, status=status.HTTP_200_OK, safe=False)
        new_player = player_serializer.save()
        response = {
            "id": new_player.id,
            "name": new_player.name,
            "position": new_player.position,
        }
        player_skills = request.data.get("playerSkills", [])
        saved_skills = []
        for a_skill in player_skills:
            a_skill["player_id"] = new_player.id
            player_skill = None
            try:
                player_skill = PlayerSkill.objects.get(player=new_player, skill=a_skill["skill"])
                player_skill_serializer = PlayerSkillSerializer(player_skill, data=a_skill, partial=True)
                if player_skill_serializer.is_valid():
                    skill_ = player_skill_serializer.validated_data["skill"]
                    if skill_ not in Constant.skills:
                        transaction.set_rollback(True)
                        return JsonResponse({"message":f"Invalid value for skill: {skill_}"}, status=status.HTTP_200_OK, safe=False)
                    player_skill.value = a_skill["value"]
                    player_skill.save()
                    saved_skills.append({
                        "id": player_skill.id,
                        "skill": player_skill.skill,
                        "value": player_skill.value,
                        "playerId": new_player.id,
                    })
                elif player_serializer.errors:
                    transaction.set_rollback(True)
                    return JsonResponse({"message":get_serializer_error(player_serializer)}, status=status.HTTP_200_OK, safe=False)
                else:
                    return JsonResponse({"message":"Invalid request body"}, status=status.HTTP_400_BAD_REQUEST, safe=False)  
            except:
                player_skill_serializer = PlayerSkillSerializer(data=a_skill)
                if player_skill_serializer.is_valid():
                    skill_ = player_skill_serializer.validated_data["skill"]
                    if skill_ not in Constant.skills:
                        transaction.set_rollback(True)
                        return JsonResponse({"message":f"Invalid value for skill: {skill_}"}, status=status.HTTP_200_OK, safe=False)
                    new_player_skill = PlayerSkill(player=new_player, skill=a_skill["skill"], value=a_skill["value"])
                    new_player_skill.save()
                    saved_skills.append({
                        "id": new_player_skill.id,
                        "skill": new_player_skill.skill,
                        "value": new_player_skill.value,
                        "playerId": new_player.id,
                    })
                elif player_serializer.errors:
                    transaction.set_rollback(True)
                    return JsonResponse({"message":get_serializer_error(player_serializer)}, status=status.HTTP_200_OK, safe=False)
                else:
                    return JsonResponse({"message":"Invalid request body"}, status=status.HTTP_400_BAD_REQUEST, safe=False)  
        response.update({
            "playerSkills":saved_skills,
        })
        return JsonResponse(response, status=status.HTTP_200_OK, safe=False)
    elif player_serializer.errors:
        return JsonResponse({"message":get_serializer_error(player_serializer)}, status=status.HTTP_200_OK, safe=False)
    else:
        pass
    return JsonResponse({"message":"Invalid request body"}, status=status.HTTP_400_BAD_REQUEST, safe=False)
