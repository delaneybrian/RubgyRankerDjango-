from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Article
from elo.serializers import FullArticleSerializer
from rest_framework import status


@api_view(['GET'])
def get_article(request, pk, format=None):
        try:
            article = Article.objects.get(pk=pk)
            serializer = FullArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            content = "Article Not Found"
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except:
            content = "Server Error"
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

