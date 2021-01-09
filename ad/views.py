from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ad, Author, Developer
from workers.models import Realtor, Position
from .serializers import AdListSerializer, AdDetailSerializer, СonvenienceCreateSerializer, AuthorListSerializer, DeveloperListSerializer

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

class AuthorListView(APIView):
  """Вывод списка авторов объявлений"""
  def get(self, request):
    authors = Author.objects.filter()
    serializer = AuthorListSerializer(authors, many=True)
    return Response(serializer.data)

class DeveloperListView(APIView):
  """Вывод списка застройщиков"""
  def get(self, request):
    developers = Developer.objects.filter()
    serializer = DeveloperListSerializer(developers, many=True)
    return Response(serializer.data)