from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Team, Match, Rivals
from elo.serializers import TeamSerializer, MatchSerializer, RivalsSerializer, MatchLargeSerializer, MatchDiagramSerializer
from django.db.models import Q, F
import json
import datetime

#GET DETAILS OF A SPECIFIC TEAM
@api_view(['GET'])
def get_team_detail(request, pk, format=None):
    try:
        team = Team.objects.get(pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    except Team.DoesNotExist:
        content = "Team Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#GET LIST OF LATEST GAMES FOR A SPECIFIC TEAM
@api_view(['GET'])
def get_latest_matches(request, pk, format=None):
    try:
        matches = Match.objects.filter(Q(awayteam=pk) | Q(hometeam=pk)).order_by('-match_date')[:10]
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)
    except Match.DoesNotExist:
        content = "Matches Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
    except Match.DoesNotExist:
        content = "Matches Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#GET RIVALS TABLE FOR SPECIFIC TEAM
@api_view(['GET'])
def get_team_rivals(request, pk, format=None):
    try:
        teams_rivals = Rivals.objects.filter(team_a=pk).order_by('team_b__name')
        serializer = RivalsSerializer(teams_rivals, many=True)
        return Response(serializer.data)
    except Rivals.DoesNotExist:
        content = "Rivals Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#GET ALL RANKED MATCHES FOR A TEAM
@api_view(['GET'])
def get_all_matches(request, pk, format=None):
    try:
        matches = Match.objects.filter(Q(awayteam=pk) | Q(hometeam=pk)).order_by('-match_date')
        serializer = MatchLargeSerializer(matches, many=True)
        return Response(serializer.data)
    except Match.DoesNotExist:
        content = "Matches Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#GET RANKING HISTORY FOR A TEAM
@api_view(['GET'])
def get_team_ranking_history(request, pk, format=None):
    try:
        array_of_tuples = []
        homematches = Match.objects.filter(hometeam=pk)
        for match in homematches:
            if int(match.hometeam.id) == int(pk):
                matchtup = (match.match_date.date(), match.hometeam.id, match.hometeam_rating_after)
                array_of_tuples.append(matchtup)
        awaymatches = Match.objects.filter(awayteam=pk)
        for match in awaymatches:
            if int(match.awayteam.id) == int(pk):
                matchtup = (match.match_date.date(), match.awayteam.id, match.awayteam_rating_after)
                array_of_tuples.append(matchtup)

        #sort array of tuples by date
        array_of_tuples = sorted(array_of_tuples, key=lambda tup: tup[0]) #reverse=True

        list_of_dicts = []
        for tuple in array_of_tuples:
            print(tuple[0])
            datadict = {
                "date" : str(tuple[0]),
                "teamid" : tuple[1],
                "rating" : tuple[2]
            }
            list_of_dicts.append(datadict)

        dict = json.dumps(list_of_dicts)
        return Response(dict)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")
