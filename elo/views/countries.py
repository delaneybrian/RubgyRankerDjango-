from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import Country
from elo.serializers import CountrySerializer

@api_view(['GET'])
def get_countries(request, format=None):
        try:
            countries = Country.objects.all()
            serializer = CountrySerializer(countries, many=True)
            return Response(serializer.data)
        except:
            print("Error: Getting List of Countries")
            dict = {}
            return Response(dict)
