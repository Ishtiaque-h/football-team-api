from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from ...models.player import Player
from ...serializers.player import PlayerSerializer

def get_player_list_handler(request: Request):
    players = Player.objects.all().order_by("id")
    player_serializer = PlayerSerializer(players, many=True)
    return JsonResponse(player_serializer.data, status=status.HTTP_200_OK, safe=False)
