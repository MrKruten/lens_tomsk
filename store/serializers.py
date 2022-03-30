from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.ImageField()

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    categories = serializers.CharField()