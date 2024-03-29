from rest_framework import serializers

from .models import Category, Basket, OrderProduct, Order, Bonus, UserInfo, ImageProduct, Discount, OptionValue, Manufacture, Product, Option, Characteristic, SubCategory, Favourites


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
    subcategories = SubCategorySerializerOnlyName(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories', 'image']


class CategorySerializerForProduct(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


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


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'percentage', 'date_start', 'date_end', 'product')


class DiscountSerializerForProduct(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('percentage', 'date_start', 'date_end')


class ProductSerializer(serializers.ModelSerializer):
    option = OptionSerializerForProduct(read_only=True, many=True)
    images = ImageProductSerializerOnlyName(many=True, read_only=True)
    subcategory = SubCategorySerializerOnlyName(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name')
    manufacture_name = serializers.CharField(source='manufacture.name')
    discounts = DiscountSerializerForProduct(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'quantity', 'manufacture_name', 'category_name',
                  'subcategory', 'option', 'images', 'isRecommended', 'discounts')


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('id', 'name', 'description', 'product')


class OptionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionValue
        fields = ('id', 'option', 'value')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = (
            'id', 'user', 'patronymic', 'telephone', 'date_of_birth', 'country', 'region', 'city', 'address', 'avatar')


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ('id', 'user', 'quantity', 'date_start', 'date_end')


class OrderProductSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'quantity', 'old_price', 'result')

    def get_result(self, instance, *args):
        result = instance.quantity * instance.old_price
        return result


class OrderProductSerializerForOrderInfo(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity', 'result')

    def get_result(self, instance, *args):
        result = instance.quantity * instance.old_price
        return result


class OrderSerializer(serializers.ModelSerializer):
    products_in_order = OrderProductSerializerForOrderInfo(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'order_date', 'user', 'products_in_order')


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id', 'product', 'user')


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ('id', 'product', 'user')
