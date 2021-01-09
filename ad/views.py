from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ad
from .serializers import AdListSerializer, AdDetailSerializer, СonvenienceCreateSerializer

class AdListView(APIView):
  """Вывод списка объявлений"""
  def get(self, request):
    ads = Ad.objects.filter()
    serializer = AdListSerializer(ads, many=True)
    return Response(serializer.data)

class AdDetailView(APIView):
  """Вывод одного объявления"""
  def get(self, request, pk):
    ads = Ad.objects.get(id=pk)
    serializer = AdDetailSerializer(ads)
    return Response(serializer.data)

class СonvenienceCreateView(APIView):
  """Добавление нового удобства"""
  def post(self, request):
    convenience = СonvenienceCreateSerializer(data=request.data)
    if convenience.is_valid():
      convenience.save()
    return Response(status=201)