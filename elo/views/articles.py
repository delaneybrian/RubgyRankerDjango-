from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Article
from elo.serializers import SmallArticleSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
import html.parser


@api_view(['GET'])
def get_articles(request, format=None):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    articles = Article.objects.all().order_by('-date')
    result_page = paginator.paginate_queryset(articles, request)
    serializer = SmallArticleSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
