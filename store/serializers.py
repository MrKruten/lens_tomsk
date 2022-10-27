from rest_framework import serializers

# class CategorySerializer(serializers.Serializer):
#   name = serializers.CharField()
#  image = serializers.ImageField()
from .models import Category, Basket, OrderProduct, Order, Bonus, UserInfo, ImageProduct, Discount, OptionValue, \
    Manufacture, Product, Option, Characteristic, SubCategory


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacture
        fields = ('id', 'name')


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name")

    class Meta:
        model = SubCategory
        fields = ['id', 'name', "category_name"]


class SubCategorySerializerOnlyName(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    subcat = SubCategorySerializerOnlyName(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcat', 'image')


class CategorySerializerForProduct(serializers.ModelSerializer):
    # subcategories = SubCategorySerializerOnlyName(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        # ['name', 'subcategories']


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


class ImageProductSerializerOnlyName(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    option = OptionSerializerForProduct(read_only=True, many=True)
    images = ImageProductSerializerOnlyName(many=True, read_only=True)
    # subcategories = SubCategorySerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name')
    manufacture_name = serializers.CharField(source='manufacture.name')

    # subcat = CategorySerializerForProduct(many=True, read_only=True)

    # categories = CategorySerializerForProduct(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'quantity', 'manufacture_name', 'category_name', 'option',
                  'images', 'isRecommended')


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
