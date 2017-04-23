from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Team, Match, Rivals
from elo.serializers import TeamSerializer, MatchSerializer, RivalsSerializer
from django.db.models import Q, F, Max, Min

#GET DETAILS OF A SPECIFIC TEAM
@api_view(['GET'])
def get_team_detail(request, pk, format=None):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return Response(serializer.data)

#GET LIST OF LATEST HOMEGAMES FOR A SPECIFIC TEAM
@api_view(['GET'])
def get_latest_home_matches(request, pk, format=None):
    matches = Match.objects.filter(hometeam=pk).order_by('-match_date')[:5]
    serializer = MatchSerializer(matches, many=True)
    return Response(serializer.data)

#GET LIST OF LATEST AWAYGAMES FOR A SPECIFIC TEAM
@api_view(['GET'])
def get_latest_away_matches(request, pk, format=None):
    matches = Match.objects.filter(awayteam=pk).order_by('-match_date')[:5]
    serializer = MatchSerializer(matches, many=True)
    return Response(serializer.data)


#GET SOME INTERESTING DATA ON A SPECIFIC TEAM
@api_view(['GET'])
def get_team_information(request, pk, format=None):
    try:
        #CALCULATE HOME MATCH WINS ETC
        home_matches = Match.objects.filter(Q(hometeam_id=pk)).count()
        won_home = Match.objects.filter(hometeam_id=pk, hometeam_score__gt=F('awayteam_score')).count()
        drew_home = Match.objects.filter(hometeam_id=pk, hometeam_score=F('awayteam_score')).count()
        lost_home = home_matches - won_home - drew_home
        home_win_precentage = (won_home / home_matches)*100

        #CALCULATE AWAY MATCH WINS ETC
        away_matches = Match.objects.filter(Q(awayteam_id=pk)).count()
        won_away = Match.objects.filter(awayteam_id=pk, awayteam_score__gt=F('hometeam_score')).count()
        drew_away = Match.objects.filter(awayteam_id=pk, awayteam_score=F('hometeam_score')).count()
        lost_away = away_matches - won_away - drew_away
        away_win_precentage = (won_away / away_matches)*100

        dict = {"home_matches" : home_matches, "won_home" : won_home, "drew_home" : drew_home, "lost_home" : lost_home, "home_win_precentage" : home_win_precentage,
                "away_matches" : away_matches, "won_away" : won_away, "drew_away": drew_away, "lost_away": lost_away, "away_win_precentage": away_win_precentage}
        return Response(dict)
    except:
        dict = {}
        print("ERROR")
        return Response(dict)


#GET RIVALS TABLE FOR SPECIFIC TEAM
@api_view(['GET'])
def get_team_rivals(request, pk, format=None):
    try:
        teams_rivals = Rivals.objects.filter(team_a=pk).order_by('team_b__name')
        serializer = RivalsSerializer(teams_rivals, many=True)
        return Response(serializer.data)
    except:
        dict = {}
        print("ERROR")
        return Response(dict)
