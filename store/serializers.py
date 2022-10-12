from rest_framework import serializers

# class CategorySerializer(serializers.Serializer):
#   name = serializers.CharField()
#  image = serializers.ImageField()
from .models import Category, Basket, OrderProduct, Order, Bonus, UserInfo, ImageProduct, Discount, OptionValue, \
    Manufacture, Product, Option, Characteristic


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacture
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class CategorySerializerForProduct(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'name')


class OptionSerializerForProduct(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['name']


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ['id', 'image', 'product']


class ImageProductSerializerForProduct(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    options = OptionSerializerForProduct(read_only=True, many=True)
    categories = CategorySerializerForProduct(read_only=True, many=True)
    images = ImageProductSerializerForProduct(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'quantity', 'manufacture', 'categories', 'options', 'images')


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('id', 'name', 'description', 'product')


class OptionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionValue
        fields = ('id', 'option', 'value')


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'percentage', 'date_start', 'date_end', 'product')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = (
        'id', 'user', 'patronymic', 'telephone', 'date_of_birth', 'country', 'region', 'city', 'address', 'avatar')


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ('id', 'user', 'quantity', 'date_start', 'date_end')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'order_date', 'user')


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'quantity')


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id', 'product', 'user')
