from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ipware import get_client_ip

from app.models import RandomNumbers
from app.serializers import RandomNumberSerializer
import random
# Create your views here.

def gen_rand():
    return random.randint(20, 50)

class RandomNumbersView(APIView):
    def get(self, request):
        ip = get_client_ip(request)
        serialized_data = RandomNumberSerializer(RandomNumbers.objects.all(), many=True).data

        return Response(data={"message": "Your ip is "+ ip[0], 'data': serialized_data, 'status': True})

    def post(self, request):
        ip = get_client_ip(request)[0]
        obj = RandomNumbers.objects.create(
            number1=gen_rand(),
            number2=gen_rand(),
            number3=gen_rand(),
            number4=gen_rand(),
            number5=gen_rand(),
            ip=ip
        )
        return Response(data={
            "message": "Random Numbers Stored",
            "status": True
        }, status=201)

    def delete(self, request):
        deleted = RandomNumbers.objects.earliest('id').delete()
        return Response(data={
            'message': 'Deleted all datas',
            'status': True
        }, status=200)