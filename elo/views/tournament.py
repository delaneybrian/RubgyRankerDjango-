from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Match, Tournament, Team
from elo.serializers import TournamentSerializer, MatchSerializer, TeamShortSerializer

#GET DETAILS OF A SPECIFIED TOURNAMENT
@api_view(['GET'])
def get_tournament_details(request, pk, format=None):
    try:
        tournament = Tournament.objects.get(pk=pk)
        serializer = TournamentSerializer(tournament)
        return Response(serializer.data)
    except:
        print("Error")
        dict = {}
        return Response(dict)


#GET RECENT MATCHES FOR A SPECIFIED TOURNAMENT
@api_view(['GET'])
def get_touramanet_matches(request, pk, format=None):
    try:
        matches = Match.objects.filter(tournament=pk).order_by('-match_date')[:10]
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)
    except:
        print("Error")
        dict = {}
        return Response(dict)


@api_view(['GET'])
def get_team_list_by_tournament(request,pk, format=None):
    try:
        teams = Team.objects.filter(tournaments=pk).order_by('thisweek_position')
        serializer = TeamShortSerializer(teams, many=True)
        return Response(serializer.data)
    except:
        print("Error: Error Getting Ranked Teams For Tournament")
        dict = {}
        return Response(dict)