from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
class CategoryView(APIView):
    def get(self, request):
        categorys = Category.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = CategorySerializer(categorys, many=True)
        return Response({"categorys": serializer.data})
