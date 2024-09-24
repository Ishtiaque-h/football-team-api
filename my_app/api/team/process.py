from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from django.db.models import Max
from ...models.values import Constant
from ...models.player import Player
from ...models.player_skill import PlayerSkill
from ...serializers.player import PlayerForTeamSerializer

def handle_values(requirement, field_):
    compare_to = Constant.positions
    if field_=="mainSkill":
        compare_to = Constant.skills
    if field_ not in requirement:
        return False, f"{field_} not given"
    elif str(requirement[field_]).strip()=="":
        return False, f"{field_} is required"
    elif field_=="numberOfPlayers" and requirement[field_]<=0:
        return False, "Invalid value for: numberOfPlayers"
    elif field_!="numberOfPlayers" and requirement[field_] not in compare_to:
        return False, f"Invalid value for {field_}: {requirement[field_].strip()}"
    return True, ""


def team_process_handler(request: Request):
    request_keys = {}
    requirements = request.data
    team_players = []
    for a_requirement in requirements:
        position_ = a_requirement["position"].strip()
        mainSkill_ = a_requirement["mainSkill"].strip()
        no_of_players = a_requirement["numberOfPlayers"]
        for a_field in ("position", "mainSkill", "numberOfPlayers"):
            is_correct, message_ = handle_values(a_requirement, a_field)
            if not is_correct:
                return JsonResponse({"message":message_}, status=status.HTTP_400_BAD_REQUEST, safe=False)
        if position_+"-"+mainSkill_ in request_keys:
            message_ = f"Same parameter given twice for position: {position_} and mainSkill: {mainSkill_}"
            return JsonResponse({"message":message_}, status=status.HTTP_400_BAD_REQUEST, safe=False)
        else:
            request_keys[position_+"-"+mainSkill_] = 1
        the_players = list(PlayerSkill.objects.filter(player__position=position_, skill=mainSkill_).values_list('player', flat=True).distinct().order_by("-value")[:no_of_players])
        if len(the_players)<no_of_players:
            extra_players = list(PlayerSkill.objects.filter(player__position=position_).exclude(player__id__in=the_players).values("player").annotate(max_value_per_player=Max("value")).order_by("-max_value_per_player").values_list("player", flat=True)[:no_of_players-len(the_players)])
            the_players = (the_players+extra_players)
        if len(the_players)<no_of_players:
            return JsonResponse({"message":f"Insufficient number of players for position: {position_}"}, status=status.HTTP_200_OK, safe=False)
        players = Player.objects.filter(pk__in=the_players).order_by("position")
        player_serializer = PlayerForTeamSerializer(players, many=True)
        team_players = (team_players+player_serializer.data)
    return JsonResponse(team_players, status=status.HTTP_200_OK, safe=False)
