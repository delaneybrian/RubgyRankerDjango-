from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Tournament
from elo.serializers import TournamentShortSerializer

@api_view(['GET'])
def get_tournaments(request, format=None):
    tournaments = Tournament.objects.all()
    serializer = TournamentShortSerializer(tournaments, many=True)
    return Response(serializer.data)