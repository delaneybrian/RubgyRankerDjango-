from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Team, Match, Tournament, Country, Rivals
from elo.serializers import  TeamShortSerializer, TournamentShortSerializer, CountrySerializer, RivalsSerializer
from django.db.models import F
from django.db.models import Q
from rest_framework import status
import elo


#GET Country
@api_view(['GET'])
def get_country_basic(request, pk, format=None):
    try:
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    except Country.DoesNotExist:
        content = "Country Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#GET LIST OF TEAMS BY COUNTRY
@api_view(['GET'])
def get_team_list_by_country(request, pk, format=None):
    try:
        teams = Team.objects.filter(country=pk).order_by("-name")
        serializer = TeamShortSerializer(teams, many=True)
        return Response(serializer.data)
    except Team.DoesNotExist:
        content = "Team Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#GET LIST OF COMPENTITIONS THAT A COUNTRY IS PART OF
@api_view(['GET'])
def get_tournament_list_by_country(request, pk, format=None):
    try:
        tournaments = Tournament.objects.filter(countries=pk)
        serializer = TournamentShortSerializer(tournaments, many=True)
        return Response(serializer.data)
    except Tournament.DoesNotExist:
        content = "Tournament Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#GET COUNTRY Stat Information
@api_view(['GET'])
def get_country_information(request, pk, format=None):
    try:
        #number of teams in a country
        num_teams_in_country = Team.objects.filter(country=pk).count()

        # home record for country against other countries
        home_matches_for_country = Match.objects.filter(Q(hometeam__country=pk), (~Q(awayteam__country=pk))).count()
        won_home = Match.objects.filter(Q(hometeam__country=pk), (~Q(awayteam__country=pk)), hometeam_score__gt=F('awayteam_score')).count()
        drew_home = Match.objects.filter(Q(hometeam__country=pk), (~Q(awayteam__country=pk)), hometeam_score=F('awayteam_score')).count()
        lost_home = home_matches_for_country - won_home - drew_home
        country_home_win_precentage = (won_home / home_matches_for_country)*100

        # away record for country against other countries
        away_matches_for_country = Match.objects.filter(Q(awayteam__country=pk), (~Q(hometeam__country=pk))).count()
        won_away = Match.objects.filter(Q(awayteam__country=pk), (~Q(hometeam__country=pk)), awayteam_score__gt=F('hometeam_score')).count()
        drew_away = Match.objects.filter(Q(awayteam__country=pk), (~Q(hometeam__country=pk)), awayteam_score=F('hometeam_score')).count()
        lost_away = away_matches_for_country - won_away - drew_away
        country_away_win_precentage = (won_away / away_matches_for_country)*100

        print(home_matches_for_country, won_home, drew_home, lost_home, country_home_win_precentage)
        print(away_matches_for_country, won_away, drew_away, lost_away, country_away_win_precentage)

        #print(home_matches_for_country, won_home, drew_home, lost_home, country_home_win_precentage)
        #print(away_matches_for_country, won_away, drew_away, lost_away, country_away_win_precentage)

        dict = {"country_home_win_precentage" : country_home_win_precentage, "country_away_win_precentage": country_away_win_precentage, }
        return Response(dict)
    except Match.DoesNotExist:
        content = "Match Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except:
        content = "Server Error"
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)