from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Team, Match, Tournament
from elo.serializers import MatchSerializer, TeamSerializer, TeamRankingSerializer
import random
from django.db.models import Max, Min


@api_view(['GET'])
def get_rankings_list(request, format=None):
        try:
            teamsRankings = Team.objects.filter(active=True).order_by('thisweek_position')[:15]
            serializer = TeamRankingSerializer(teamsRankings, many=True)
            return Response(serializer.data)
        except:
            print("Error: Error 2 Getting Ratings List")
            dict = {}
            return Response(dict)


#EXTRA INFORMATION
@api_view(['GET'])
def get_rankings_detail(request, format=None):
    try:
        no_teams = Team.objects.filter(active=True).count()
        no_matches = Match.objects.filter(hometeam__active=True, awayteam__active=True).count()
        no_tournaments = Tournament.objects.count()
        latest_match = Match.objects.all().aggregate(Max('match_date'))
        first_match = Match.objects.all().aggregate(Min('match_date'))
        dict = {"Teams" : no_teams, "Matches" : no_matches, "Tournaments" : no_tournaments, "FirstMatch" : first_match['match_date__min'], "LastMatch" : latest_match['match_date__max']}
        return Response(dict)
    except:
        print("Error: Cannot Execute Command For Obtaining Ranking System Details")
        dict = {}
        return Response(dict)


# GET LIST OF LATEST MATCHES
@api_view(['GET'])
def get_latest_matches(request, format=None):
    try:
        matches = Match.objects.all().order_by('-match_date')[:5]
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)
    except:
        print("Error: Could Not Get Latest Matches")
        dict = {}

        return Response(dict)


#GET FEATURED TEAM
@api_view(['GET'])
def get_featured_team(request, format=None):
    try:
        ids = Team.objects.raw("SELECT id FROM elo_team WHERE active=true;")
        id_store = []
        for id in ids:
            id_store.append(id.id)
        pk = random.choice(id_store)
        print(pk)
        team = Team.objects.get(pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    except:
        print("Error: Error Getting Random Team")
        dict = {}
        return Response(dict)

