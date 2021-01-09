from rest_framework import serializers

from .models import Ad, Сonvenience, Price

class AdListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ad
    fields = ("title", "description", "address")


class PriceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Price
    fields = ("newPricece", "updatedAt")


class AdDetailSerializer(serializers.ModelSerializer):
  author = serializers.SlugRelatedField(slug_field="name", read_only=True)
  typeOfArea = serializers.SlugRelatedField(slug_field="name", read_only=True)
  typeOfAd = serializers.SlugRelatedField(slug_field="name", read_only=True)
  developer = serializers.SlugRelatedField(slug_field="name", read_only=True)
  realtor = serializers.SlugRelatedField(slug_field="name", read_only=True)
  convenience = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)
  price = PriceSerializer(many=True)

  class Meta:
    model = Ad
    fields = "__all__"


class СonvenienceCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Сonvenience
    fields = "__all__"
