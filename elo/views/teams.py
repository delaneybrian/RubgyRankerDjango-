from rest_framework.decorators import api_view
from elo.models import Team
from elo.serializers import TeamShortSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


@api_view(['GET'])
def get_team_list(request, format=None):
    paginator = PageNumberPagination()
    paginator.page_size = 25
    teams = Team.objects.filter(active=True).order_by('name')
    result_page = paginator.paginate_queryset(teams, request)
    serializer = TeamShortSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def search_team_by_name(request, format=None):
    #try:
        dict = {}
        searchString = (request.GET.get('team'))
        print(searchString)
        teams = Team.objects.filter(name__icontains=searchString, active=True)
        #selectString = "SELECT * FROM elo_team WHERE name LIKE '%Mun%';"
        #teams= Team.objects.raw(selectString)
        print(teams)
        serializer = TeamShortSerializer(teams, many=True)
        print("SERIALIZER")
        print(serializer)
        print("END SERIALIZER")
        return Response(serializer.data)
    #except:
    #    dict = {}
    #    print("ERROR")
    #    return Response(dict)