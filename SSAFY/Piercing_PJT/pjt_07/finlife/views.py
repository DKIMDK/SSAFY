from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from django.http import JsonResponse
from .models import DepositOptions, DepositProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"

    response = requests.get(url).json()


    for li in response.get("list"):
        save_data = {
            'dt_txt' : li.get('dt_txt'),
            'temp' : li.get('main').get('temp'),
            'feels_like' : li.get('main').get('feels_like'),
        }
        serializer = DepositProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({"message":"okay"})

@api_view(["GET"])
def list_data(request):
    depositproducts = DepositProducts.obejcts.all()
    serializer = DepositProductsSerializer(depositproducts, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def hot_weathers(request):
    weathers = DepositProducts.objects.all()
    hot_weathers = []
    for weather in weathers:
        tmp = round(DepositProducts ...)
        if tmp > 30:
            hot_weathers.append(weather)

    serializer = DepositProductsSerializer(hot_weathers, many=True)
    return Response(serializer.data)