from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

def index(request):
    return render(request, 'index.html')

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories": serializer.data})

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})
