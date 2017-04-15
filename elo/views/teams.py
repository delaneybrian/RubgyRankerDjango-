from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Team
from elo.serializers import TeamShortSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_team_list(request, format=None):
    paginator = PageNumberPagination()
    paginator.page_size = 25
    teams = Team.objects.filter(active=True).order_by('name')
    result_page = paginator.paginate_queryset(teams, request)
    serializer = TeamShortSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
