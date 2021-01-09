from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Realtor, Position

from .serializers import RealtorListSerializer, RealtorDetailSerializer, PositionListSerializer

class RealtorListView(APIView):
  """Вывод списка риеэторов"""
  def get(self, request):
    realtors = Realtor.objects.filter()
    serializer = RealtorListSerializer(realtors, many=True)
    return Response(serializer.data)

class RealtorDetailView(APIView):
  """Вывод одного риелтора"""
  def get(self, request, pk):
    realtors = Realtor.objects.get(id=pk)
    serializer = RealtorDetailSerializer(realtors)
    return Response(serializer.data)

class PositionListView(APIView):
  """Вывод списка должностей"""
  def get(self, request):
    positions = Position.objects.filter()
    serializer = PositionListSerializer(positions, many=True)
    return Response(serializer.data)
