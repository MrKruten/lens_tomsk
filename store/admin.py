from django.contrib import admin
from .models import Manufacture, Category, Bonus, Basket, UserInfo, Discount, Characteristic, OrderProduct, Order, \
    Option, ImageProduct, Product, OptionValue, SubCategory

admin.site.register(ImageProduct)


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_filter = ['name']
    inlines = [ProductInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['name']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_filter = ['name']


class ImageProductInline(admin.TabularInline):
    model = ImageProduct


class DiscountInline(admin.TabularInline):
    model = Discount


class CharacteristicInline(admin.TabularInline):
    model = Characteristic


class OptionValueInline(admin.TabularInline):
    model = OptionValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('price', 'quantity', 'name')
    inlines = [ImageProductInline, DiscountInline, CharacteristicInline]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_filter = ('name', 'product')
    inlines = [OptionValueInline]


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_filter = ('name', 'product')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_filter = ('date_start', 'date_end', 'percentage')


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_filter = ('date_of_birth', 'country', 'region', 'city')


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_filter = ('date_start', 'date_end', 'quantity', 'user')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('order_date', 'user')


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_filter = ('order', 'product', 'quantity')
