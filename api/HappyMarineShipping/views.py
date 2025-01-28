from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import random
from django.utils.timezone import now,localtime

from .serializers import RegSgipForSaleSerializer
from web.models import RegisterShipForSale

@api_view(['POST'])
@permission_classes([AllowAny])
def AddShip(request):
   data=request.data
   ship=RegSgipForSaleSerializer(data=data)
   print(data)
   if ship.is_valid():
        ship.save()
        response_data={
            "status":200,
            "message":"Ship registered Successfully"
        }
   else:
       response_data={
            "Status":201,
            "message":"data not Added"
        }
   return Response(response_data)



@api_view(['GET'])
@permission_classes([AllowAny])
def AllShips(request):
    title=request.GET.get('title')
    context={
        "request":request
    }
    if title:
        ships = RegisterShipForSale.objects.filter(title__icontains=title)
    else:
        ships = RegisterShipForSale.objects.all()  
    serializer = RegSgipForSaleSerializer(instance=ships, many=True,context=context)
    if serializer:
        response_data = {
        "status": 200,
        "data": serializer.data
        }
    else:
            response_data = {
            "Status": 201,
            "message": "data not found",
            }
    return Response(response_data)