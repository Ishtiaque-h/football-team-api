from rest_framework.test import APITestCase, RequestsClient

from ..models.player import Player
from ..models.player_skill import PlayerSkill

class UpdatePlayerTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Player.objects.all().delete()
        PlayerSkill.objects.all().delete()

    def test_sample(self):
        data = {
            'name': 'player name updated',
            'position': 'midfielder',
            'playerSkills': [
                {
                    'skill': 'strength',
                    'value': 40
                },
                {
                    'skill': 'stamina',
                    'value': 30
                }
            ]
        }

        response = self.client.put('http://127.0.0.1:8000/api/player/2')
        self.assertIsNotNone(response)
