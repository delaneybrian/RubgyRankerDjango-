from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Team
from elo.serializers import TeamRankingSerializer
import operator
from operator import itemgetter


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



@api_view(['GET'])
def get_gains_losses(request, format=None):
    #try:
        teams = Team.objects.raw("SELECT id, thisweek_position, lastweek_position FROM elo_team WHERE active=True;")
        teamarray = []
        for team in teams:
            #Negative for gains Positive for Falls
            difference = int(team.thisweek_position) - int(team.lastweek_position)
            teamDict = {"id" : int(team.id), "difference" : int(difference)}
            teamarray.append(teamDict)

        newlist = sorted(teamarray, key=itemgetter('difference'))
        listlength = len(newlist)

        biggestGain = (newlist[0])
        biggestLoss = (newlist[listlength - 1])


        biggestGainTeam = Team.objects.get(id=(int(biggestGain["id"])))
        biggestLossTeam = Team.objects.get(id=(int(biggestLoss["id"])))


        biggestGainTeamSerializer = TeamRankingSerializer(biggestGainTeam)
        biggestLossTeamSerializer = TeamRankingSerializer(biggestLossTeam)

        dict = {"biggestGain" : biggestGainTeamSerializer.data, "biggestLoss" : biggestLossTeamSerializer.data}
        return Response(dict)
    #except:
       # print('Error: Error Getting Biggest Faller and Gainer')
       # dict = {}
        #return Response(dict)