from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from typing import Any
from django.conf import settings
from ...models import Player


def delete_player_handler(request: Request, id: Any):
    if not ('HTTP_AUTHORIZATION' in request.META.keys()):
        return JsonResponse({"message":"No Authorization Token given"}, status=status.HTTP_401_UNAUTHORIZED, safe=False)
    elif (request.META['HTTP_AUTHORIZATION'].strip() == settings.AUTHORIZATION_TOKEN):
        try:
            player = Player.objects.get(pk=id)
            player.delete()
            """
                Don't need to delete skills separately as skills are cascaded with the player
            """
            return JsonResponse({"message":"Player data deleted successfully"}, status=status.HTTP_404_NOT_FOUND, safe=False)   
        except Player.DoesNotExist:
            return JsonResponse({"message":"Player not found"}, status=status.HTTP_404_NOT_FOUND, safe=False)   
        except:
            pass
        return JsonResponse({"message":"Could not delete data"}, status=status.HTTP_200_OK, safe=False)
    else:
        pass
    return JsonResponse({"message":"Invalid Authorization Token!"}, status=status.HTTP_401_UNAUTHORIZED, safe=False)
