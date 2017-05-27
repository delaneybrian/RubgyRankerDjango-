from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Team, Match, Rivals
from elo.serializers import TeamSerializer, MatchSerializer, RivalsSerializer, MatchLargeSerializer, MatchDiagramSerializer
from django.db.models import Q, F
import json
import sys
import datetime

#http://localhost:8000/api/comparison/?teamA=1&teamB=3

#GET DETAILS OF A SPECIFIC TEAM
@api_view(['GET'])
def getMainDetails(request, format=None):

    toreturn = {}

    #ENSURE VALUES ARE CORRECT AND NUMERIC
    try:
        teamAid = int(request.GET.get('teamA'))
    except TypeError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        teamBid = int(request.GET.get('teamB'))
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except TypeError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    #TRY GET TEAMS
    try:
        team = Team.objects.get(pk=teamAid)
        serializer = TeamSerializer(team)
        teamAData = serializer.data
        toreturn["teamAData"] = teamAData
    except Team.DoesNotExist:
        content = "Team Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    try:
        team = Team.objects.get(pk=teamBid)
        serializer = TeamSerializer(team)
        teamBData = serializer.data
        toreturn["teamBData"] = teamBData
    except Team.DoesNotExist:
        content = "Team Not Found"
        return Response(content, status=status.HTTP_404_NOT_FOUND)


    #SECTION TO GET ALL MATCHES AND SCORES BETWEEN TEAMS

    allmatches = []
    teamAHomeScores = []
    teamBHomeScores = []
    teamAAwayScores = []
    teamBAwayScores = []

    try:
        try:
            teamAHomematches = Match.objects.filter(hometeam=teamAid, awayteam=teamBid, ).order_by('-match_date')
            for match in teamAHomematches:
                allmatches.append(match)
                teamAHomeScores.append(match.hometeam_score)
                teamBAwayScores.append(match.awayteam_score)
        except Match.DoesNotExist:
            print("Match Does Not Exist")
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            teamBHomematches = Match.objects.filter(hometeam=teamBid, awayteam=teamAid).order_by('-match_date')
            for match in teamBHomematches:
                allmatches.append(match)
                teamBHomeScores.append(match.hometeam_score)
                teamAAwayScores.append(match.awayteam_score)
        except Match.DoesNotExist:
            print("Match Does Not Exist")
            return Response(status=status.HTTP_400_BAD_REQUEST)

        teamAAverageHomeScore = round(sum(teamAHomeScores)/len(teamAHomeScores),2)
        teamBAverageHomeScore = round(sum(teamBHomeScores)/len(teamBHomeScores),2)
        teamAAverageAwayScore = round(sum(teamAAwayScores)/len(teamAAwayScores),2)
        teamBAverageAwayScore = round(sum(teamBAwayScores)/len(teamBAwayScores),2)

        teamAAvreageScore = round(sum(teamAHomeScores + teamAAwayScores)/len(teamAHomeScores + teamAAwayScores),2)
        teamBAvreageScore = round(sum(teamBHomeScores + teamBAwayScores)/len(teamBHomeScores + teamBAwayScores),2)

        vsScoresDict = {
                      "teamAAverageHomeScore" : teamAAverageHomeScore,
                      "teamBAverageHomeScore" : teamBAverageHomeScore,
                      "teamAAverageAwayScore" : teamAAverageAwayScore,
                      "teamBAverageAwayScore" : teamBAverageAwayScore,
                      "teamAAvreageScore" : teamAAvreageScore,
                      "teamBAvreageScore" : teamBAvreageScore
                        }

        toreturn["vsScoresDict"] = vsScoresDict
    except:
        print("Error Here")
        toreturn["vsScoresDict"] = 0;
        pass



    #GET STREAKS AND WIN RECORD VS TEAM

    teamAHomeWins = 0
    teamBHomeWins = 0
    teamAAwayWins = 0
    teamBAwayWins = 0
    draws = 0

    teamAMaxStreak = 0
    teamBMaxStreak = 0
    teamACurrentStreak = 0
    teamBCurrentStreak = 0


    try:
        allVsMatchesOrdered = Match.objects.filter(Q(hometeam=teamBid, awayteam=teamAid) | Q(hometeam=teamAid, awayteam=teamBid)).order_by('-match_date')
        # calculate head to head form
        headToHeadForm = []

        for match in allVsMatchesOrdered[:10]:

            if (match.hometeam_id == teamAid):
                if (match.hometeam_score > match.awayteam_score):
                    headToHeadForm.append("W")
                elif (match.hometeam_score < match.awayteam_score):
                    headToHeadForm.append("L")
                else:
                    headToHeadForm.append("D")

            if (match.awayteam_id == teamAid):
                if (match.awayteam_score > match.hometeam_score):
                    headToHeadForm.append("W")
                elif (match.awayteam_score < match.hometeam_score):
                    headToHeadForm.append("L")
                else:
                    headToHeadForm.append("D")

        # Add all matches to dict to return
        serializer = MatchSerializer(allVsMatchesOrdered, many=True)
        recentMatches = serializer.data

        toreturn["recentMatches"] = recentMatches


        toreturn["headToHeadForm"] = headToHeadForm

    except Match.DoesNotExist:
        print("Match Does Not Exist")
        return Response(status=status.HTTP_400_BAD_REQUEST)



    try:
        allVsMatches = Match.objects.filter(Q(hometeam=teamBid, awayteam=teamAid) | Q(hometeam=teamAid, awayteam=teamBid)).order_by('match_date')

        for match in allVsMatches:

            if(match.hometeam_id == teamAid):
                if (match.hometeam_score > match.awayteam_score):
                    teamAHomeWins += 1
                    teamACurrentStreak +=1
                    teamBCurrentStreak = 0
                    if teamACurrentStreak > teamAMaxStreak:
                        teamAMaxStreak = teamACurrentStreak
                elif (match.hometeam_score < match.awayteam_score):
                    teamBAwayWins += 1
                    teamBCurrentStreak += 1
                    teamACurrentStreak = 0
                    if teamBCurrentStreak > teamBMaxStreak:
                        teamBMaxStreak = teamBCurrentStreak
                else:
                    draws += 1
                    teamACurrentStreak = 0
                    teamBCurrentStreak = 0

            if(match.hometeam_id == teamBid):
                if (match.hometeam_score > match.awayteam_score):
                    teamBHomeWins += 1
                    teamBCurrentStreak += 1
                    teamACurrentStreak = 0
                    if teamBCurrentStreak > teamBMaxStreak:
                        teamBMaxStreak = teamBCurrentStreak
                elif (match.hometeam_score < match.awayteam_score):
                    teamAAwayWins += 1
                    teamACurrentStreak += 1
                    teamBCurrentStreak = 0
                    if teamACurrentStreak > teamAMaxStreak:
                        teamAMaxStreak = teamACurrentStreak
                else:
                    draws += 1
                    teamACurrentStreak = 0
                    teamBCurrentStreak = 0

        streakAndWins = {
                                     "teamAHomeWins": teamAHomeWins,
                                     "teamAAwayWins": teamAAwayWins,
                                     "teamAMaxStreak": teamAMaxStreak,
                                     "teamACurrentStreak": teamACurrentStreak,
                                     "teamBHomeWins": teamBHomeWins,
                                     "teamBAwayWins": teamBAwayWins,
                                     "teamBMaxStreak": teamBMaxStreak,
                                     "teamBCurrentStreak": teamBCurrentStreak,
                                     "draws": draws,
                             }
        toreturn["streakAndWins"] = streakAndWins

    except Match.DoesNotExist:
        print("Match Does Not Exist")
        return Response(status=status.HTTP_400_BAD_REQUEST)


    # GET AVERAGE POINTS ACCROSS ALL MATCHES

    teamAAllHomeScores = []
    teamAAllAwayScores = []
    teamAAllScores = []

    teamBAllHomeScores = []
    teamBAllAwayScores = []
    teamBAllScores = []

    teamAHistoricRankings = []
    teamAHistoricRankingDates = []
    teamBHistoricRankings = []
    teamBHistoricRankingDates = []

    try:
        allteamAmatches = Match.objects.filter(Q(hometeam=teamAid) | Q(awayteam=teamAid)).order_by('match_date')
        for match in allteamAmatches:
            if(match.hometeam_id == teamAid):
                teamAAllHomeScores.append(match.hometeam_score)
                teamAAllScores.append(match.hometeam_score)
                teamAHistoricRankingDates.append(match.match_date)
                teamAHistoricRankings.append(match.hometeam_rating_after)

            if (match.awayteam_id == teamAid):
                teamAAllAwayScores.append(match.awayteam_score)
                teamAAllScores.append(match.awayteam_score)
                teamAHistoricRankingDates.append(match.match_date)
                teamAHistoricRankings.append(match.awayteam_rating_after)

        allteamBmatches = Match.objects.filter(Q(hometeam=teamBid) | Q(awayteam=teamBid)).order_by('match_date')
        for match in allteamBmatches:
            if (match.hometeam_id == teamBid):
                teamBAllHomeScores.append(match.hometeam_score)
                teamBAllScores.append(match.hometeam_score)
                teamBHistoricRankingDates.append(match.match_date)
                teamBHistoricRankings.append(match.hometeam_rating_after)


            if (match.awayteam_id == teamBid):
                teamBAllAwayScores.append(match.awayteam_score)
                teamBAllScores.append(match.awayteam_score)
                teamBHistoricRankingDates.append(match.match_date)
                teamBHistoricRankings.append(match.awayteam_rating_after)





        teamAAllAverageHomeScore = round(sum(teamAAllHomeScores)/len(teamAAllHomeScores),2)
        teamAAllAverageAwayScore = round(sum(teamAAllAwayScores)/len(teamAAllAwayScores),2)
        teamAAllAverageScore = round(sum(teamAAllScores)/len(teamAAllScores),2)

        teamBAllAverageHomeScore = round(sum(teamBAllHomeScores) / len(teamBAllHomeScores),2)
        teamBAllAverageAwayScore = round(sum(teamBAllAwayScores) / len(teamBAllAwayScores),2)
        teamBAllAverageScore = round(sum(teamBAllScores) / len(teamBAllScores),2)

        sameLengthRankingTeamA = []
        sameLengthRankingTeamB = []
        sameLengthDates = []

        #CALCULATION TO ENSURE THE SAME LENGTH IN HISTORIC RANKINGS

        #step1 reverse all lists
        teamAHistoricRankingsREVERSED = []
        teamAHistoricRankingDatesREVERSED = []
        teamBHistoricRankingsREVERSED = []
        teamBHistoricRankingDatesREVERSED = []

        for i in reversed(teamAHistoricRankings):
            teamAHistoricRankingsREVERSED.append(i)
        for i in reversed(teamAHistoricRankingDates):
            teamAHistoricRankingDatesREVERSED.append(i.date())
        for i in reversed(teamBHistoricRankings):
            teamBHistoricRankingsREVERSED.append(i)
        for i in reversed(teamBHistoricRankingDates):
            teamBHistoricRankingDatesREVERSED.append(i.date())

        #MAKE LISTS THE SAME SIZE
        lengthDatesA = len(teamAHistoricRankingDatesREVERSED)
        lengthDatesB = len(teamBHistoricRankingDatesREVERSED)

        if(lengthDatesA >= lengthDatesB):
            lenToCal = lengthDatesB - 1
        else:
            lenToCal = lengthDatesA - 1

        normalizedTeamARankings = (teamAHistoricRankingsREVERSED[:lenToCal])
        normalizedTeamBRankings = (teamBHistoricRankingsREVERSED[:lenToCal])
        normalizedDates = (teamBHistoricRankingDatesREVERSED[:lenToCal])

        normalizedTeamARankingsReversed = []
        normalizedTeamBRankingsReversed = []
        normalizedDatesReversed = []

        for i in reversed(normalizedTeamARankings):
            normalizedTeamARankingsReversed.append(i)
        for i in reversed(normalizedTeamBRankings):
            normalizedTeamBRankingsReversed.append(i)
        for i in reversed(normalizedDates):
            normalizedDatesReversed.append(i)

        normailizedHistoricRatings = {
            "normalizedTeamARankings" : normalizedTeamARankingsReversed,
            "normalizedTeamBRankings" : normalizedTeamBRankingsReversed,
            "normalizedDates" : normalizedDatesReversed
        }

        toreturn["normailizedHistoricRatings"] = normailizedHistoricRatings

        historicRatings = {
            "teamAHistoricRankings" : teamAHistoricRankings,
            "teamAHistoricRankingDates" : teamAHistoricRankingDates,
            "teamBHistoricRankings" : teamBHistoricRankings,
            "teamBHistoricRankingDates" : teamBHistoricRankingDates
        }

        toreturn["historicRatings"] = historicRatings

        allGamesAverage = {
                "teamAAllAverageHomeScore": teamAAllAverageHomeScore,
                "teamAAllAverageAwayScore": teamAAllAverageAwayScore,
                "teamAAllAverageScore": teamAAllAverageScore,
                "teamBAllAverageHomeScore": teamBAllAverageHomeScore,
                "teamBAllAverageAwayScore": teamBAllAverageAwayScore,
                "teamBAllAverageScore": teamBAllAverageScore,
            }
        toreturn["allGamesAverage"] = allGamesAverage

    except Match.DoesNotExist:
        print("Match Does Not Exist")
        return Response(status=status.HTTP_400_BAD_REQUEST)

    except:
        print(sys.exc_info()[0])
        pass


    try:
        teamARecentAny = []
        teamBRecentAny = []
        lasttenteamAmatches = Match.objects.filter(Q(hometeam=teamAid) | Q(awayteam=teamAid)).order_by('-match_date')[:10]
        lasttenteamBmatches = Match.objects.filter(Q(hometeam=teamBid) | Q(awayteam=teamBid)).order_by('-match_date')[:10]

        for match in lasttenteamAmatches:
            if match.hometeam_id == teamAid:
                if match.hometeam_score > match.awayteam_score:
                    teamARecentAny.append("W")
                elif match.hometeam_score < match.awayteam_score:
                    teamARecentAny.append("L")
                else:
                    teamARecentAny.append("D")
            if match.awayteam_id == teamAid:
                if match.hometeam_score > match.awayteam_score:
                    teamARecentAny.append("L")
                elif match.hometeam_score < match.awayteam_score:
                    teamARecentAny.append("W")
                else:
                    teamARecentAny.append("D")

        for match in lasttenteamBmatches:
            if match.hometeam_id == teamBid:
                if match.hometeam_score > match.awayteam_score:
                    teamBRecentAny.append("W")
                elif match.hometeam_score < match.awayteam_score:
                    teamBRecentAny.append("L")
                else:
                    teamBRecentAny.append("D")
            if match.awayteam_id == teamBid:
                if match.hometeam_score > match.awayteam_score:
                    teamBRecentAny.append("L")
                elif match.hometeam_score < match.awayteam_score:
                    teamBRecentAny.append("W")
                else:
                    teamBRecentAny.append("D")

        recentMatchRecord = {
            "teamARecentAny" : teamARecentAny,
            "teamBRecentAny" : teamBRecentAny
        }

        toreturn["recentMatchRecord"] = recentMatchRecord

    except Match.DoesNotExist:
        print("Match Does Not Exist")
        return Response(status=status.HTTP_400_BAD_REQUEST)

    except:
        print(sys.exc_info()[0])
        pass

    return Response(toreturn)
