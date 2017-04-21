from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Team
from elo.serializers import TeamRankingSerializer

@api_view(['GET'])
def get_rankings_list(request, format=None):
        try:
            teamsRankings = Team.objects.filter(active=True).order_by('thisweek_position')
            serializer = TeamRankingSerializer(teamsRankings, many=True)
            return Response(serializer.data)
        except:
            print("Error: Error 2 Getting Ratings List")
            dict = {}
            return Response(dict)