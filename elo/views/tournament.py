from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Match, Tournament, CurrentRankingTable
from elo.serializers import TournamentSerializer, MatchSerializer, RankingSerializer

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
        rating_dates = CurrentRankingTable.objects.order_by('-date').distinct('date')[:1]
        if len(rating_dates) == 1:
            latest_date = rating_dates[0].date
            teamrankingsbycountry = CurrentRankingTable.objects.filter(date=str(latest_date), team__tournaments=pk).order_by('position')
            serializer = RankingSerializer(teamrankingsbycountry, many=True)
            return Response(serializer.data)
        else:
            print("Error: Error Getting Ranked Teams For Tournament")
            dict = {}
            return Response(dict)
    except:
        print("Error: Error Getting Ranked Teams For Tournament")
        dict = {}
        return Response(dict)