from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import CurrentRankingTable
from elo.serializers import RankingSerializer

@api_view(['GET'])
def get_rankings_list(request, format=None):
        try:
            rating_dates = CurrentRankingTable.objects.order_by('-date').distinct('date')[:1]
            if len(rating_dates) == 1:
                latest_date = rating_dates[0].date
                week_rankings = CurrentRankingTable.objects.filter(date=str(latest_date)).order_by('-rating')
                serializer = RankingSerializer(week_rankings, many=True)
                return Response(serializer.data)
            else:
                print("Error: Error 1 Getting Ratings List")
                dict = {}
                return Response(dict)
        except:
            print("Error: Error 2 Getting Ratings List")
            dict = {}
            return Response(dict)