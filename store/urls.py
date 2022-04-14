from rest_framework.routers import DefaultRouter

from .views import CategoryView, ManufactureView, OptionView, ProductView, CharacteristicView, \
    OptionValueView, DiscountView, ImageProductView, UserInfoViewSet, BonusView, OrderView, \
    OrderProductView, BasketViewSet

router = DefaultRouter()
router.register(r'manufactures', ManufactureView, basename='manufacture')
router.register(r'categories', CategoryView, basename='category')
router.register(r'options', OptionView, basename='option')
router.register(r'products', ProductView, basename='product')
router.register(r'characteristics', CharacteristicView, basename='characteristic')
router.register(r'optionsValue', OptionValueView, basename='optionValue')
router.register(r'discounts', DiscountView, basename='discount')
router.register(r'imagesProduct', ImageProductView, basename='imageProduct')
router.register(r'bonuses', BonusView, basename='bonus')
router.register(r'orders', OrderView, basename='order')
router.register(r'ordersProduct', OrderProductView, basename='orderProduct')
router.register(r'usersInfo', UserInfoViewSet, basename='userInfo')
router.register(r'baskets', BasketViewSet, basename='basket')


urlpatterns = router.urls

