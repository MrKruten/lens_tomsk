from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Manufacture, Option, Product, Characteristic, OptionValue, Discount, \
    ImageProduct, UserInfo, Bonus, Order, OrderProduct, Basket
from .serializers import ManufactureSerializer, CategorySerializer, OptionSerializer, ProductSerializer, \
    CharacteristicSerializer, OptionValueSerializer, DiscountSerializer, ImageProductSerializer, \
    UserInfoSerializer, BonusSerializer, OrderSerializer, OrderProductSerializer, BasketSerializer


def index(request):
    return render(request, 'index.html')

#////////////////////////////////////////////////////

# class ViewSet(viewsets.ModelViewSet):
#     serializer_class = Serializer
#     queryset = .objects.all()

# class View(viewsets.ViewSet):
#     def list(self, request):
#         queryset = .objects.all()
#         serializer = Serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = .objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = Serializer(user)
#         return Response(serializer.data)

#////////////////////////////////////////////////////

class ManufactureView(viewsets.ViewSet):
    def list(self, request):
        queryset = Manufacture.objects.all()
        serializer = ManufactureSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Manufacture.objects.all()
        manufacture = get_object_or_404(queryset, pk=pk)
        serializer = ManufactureSerializer(manufacture)
        return Response(serializer.data)


class CategoryView(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class OptionView(viewsets.ViewSet):
    def list(self, request):
        queryset = Option.objects.all()
        serializer = OptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Option.objects.all()
        option = get_object_or_404(queryset, pk=pk)
        serializer = OptionSerializer(option)
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CharacteristicView(viewsets.ViewSet):
    def list(self, request):
        queryset = Characteristic.objects.all()
        serializer = CharacteristicSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Characteristic.objects.all()
        characteristic = get_object_or_404(queryset, pk=pk)
        serializer = CharacteristicSerializer(characteristic)
        return Response(serializer.data)


class OptionValueView(viewsets.ViewSet):
    def list(self, request):
        queryset = OptionValue.objects.all()
        serializer = OptionValueSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = OptionValue.objects.all()
        optionValue = get_object_or_404(queryset, pk=pk)
        serializer = OptionValueSerializer(optionValue)
        return Response(serializer.data)


class DiscountView(viewsets.ViewSet):
    def list(self, request):
        queryset = Discount.objects.all()
        serializer = DiscountSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Discount.objects.all()
        discount = get_object_or_404(queryset, pk=pk)
        serializer = DiscountSerializer(discount)
        return Response(serializer.data)


class ImageProductView(viewsets.ViewSet):
    def list(self, request):
        queryset = ImageProduct.objects.all()
        serializer = ImageProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ImageProduct.objects.all()
        imageProduct = get_object_or_404(queryset, pk=pk)
        serializer = ImageProductSerializer(imageProduct)
        return Response(serializer.data)


class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()
    # def list(self, request):
    #     queryset = UserInfo.objects.all()
    #     serializer = UserInfoSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = UserInfo.objects.all()
    #     userInfo = get_object_or_404(queryset, pk=pk)
    #     serializer = UserInfoSerializer(userInfo)
    #     return Response(serializer.data)


class BonusView(viewsets.ViewSet):
    def list(self, request):
        queryset = Bonus.objects.all()
        serializer = BonusSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Bonus.objects.all()
        bonus = get_object_or_404(queryset, pk=pk)
        serializer = BonusSerializer(bonus)
        return Response(serializer.data)


class OrderView(viewsets.ViewSet):
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class OrderProductView(viewsets.ViewSet):
    def list(self, request):
        queryset = OrderProduct.objects.all()
        serializer = OrderProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = OrderProduct.objects.all()
        orderProduct = get_object_or_404(queryset, pk=pk)
        serializer = OrderProductSerializer(orderProduct)
        return Response(serializer.data)


class BasketViewSet(viewsets.ModelViewSet):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    # def list(self, request):
    #     queryset = Basket.objects.all()
    #     serializer = BasketSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Basket.objects.all()
    #     basket = get_object_or_404(queryset, pk=pk)
    #     serializer = BasketSerializer(basket)
    #     return Response(serializer.data)


