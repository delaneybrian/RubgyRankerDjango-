from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elo.models import FAQ
from elo.serializers import NewsletterSerializer, FAQSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication



#*********************FAQS PAGE ************************
#GET FAQs
@api_view(['GET'])
def get_faq(request, format=None):
    faqs = FAQ.objects.all().order_by('-importance')
    serializer = FAQSerializer(faqs, many=True)
    return Response(serializer.data)

#ADD EMAIL TO NEWLETTER
@api_view(['POST'])
def post_email(request, format=None):
    serializer = NewsletterSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        print("VALID")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("NOTVALID")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)