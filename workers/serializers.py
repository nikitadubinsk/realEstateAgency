from rest_framework import serializers

from .models import Realtor, Position

class RealtorListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Realtor
    fields = ("name", "email")

class PositionListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Position
    fields = "__all__"

class RealtorDetailSerializer(serializers.ModelSerializer):
  position = serializers.SlugRelatedField(slug_field="title", read_only=True)

  class Meta:
    model = Realtor
    fields = "__all__"
