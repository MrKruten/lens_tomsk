from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Manufacture(models.Model):
    name = models.CharField(max_length=64, help_text="Введите название компании", verbose_name="Название компании")

    class Meta:
        verbose_name_plural = "Производитель"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, help_text="Введите название категории", verbose_name="Название категории")
    image = models.ImageField(upload_to='images/categories/%Y/%m/%d/', help_text="Загрузите изображение",
                              verbose_name="Изображение категории", null=True, blank=True, )

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(help_text="Введите название опции", verbose_name="Название опции", max_length=64)

    class Meta:
        verbose_name_plural = "Опции"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, help_text="Введите название продукта", verbose_name="Название продукта")
    price = models.DecimalField(max_digits=15, decimal_places=4, help_text="Введите цену", verbose_name="Цена продукта")
    description = models.TextField(help_text="Введите описание", verbose_name="Описание продукта")
    quantity = models.PositiveIntegerField(help_text="Введите количество продукта", verbose_name="Количество продукта")
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, help_text="Выберите компанию",
                                    verbose_name="Компания")
    categories = models.ManyToManyField(Category, help_text="Выберите категории", verbose_name="Категории")
    options = models.ManyToManyField(Option, help_text="Выберите опции", verbose_name="Опции")

    class Meta:
        ordering = ["price", "quantity"]
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    name = models.TextField(help_text="Введите название характеристики", verbose_name="Название категории")
    description = models.TextField(help_text="Введите описание характеристики", verbose_name="Описание характеристики")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите продукт", verbose_name="Продукт")

    class Meta:
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return self.name


class OptionValue(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, help_text="Выберите опцию", verbose_name="Опция")
    value = models.CharField(help_text="Введите значение опции", verbose_name="Значение опции", max_length=64)

    class Meta:
        db_table = "store_option_value"
        verbose_name_plural = "Значения опций"

    def __str__(self):
        return '%s %s' % (self.option.name, self.value)


class Discount(models.Model):
    percentage = models.DecimalField(max_digits=10, decimal_places=2, help_text="Введите процент скидки",
                                     verbose_name="Процент скидки")
    date_start = models.DateField(help_text="Введите дату начала акции", verbose_name="Дата начала акции")
    date_end = models.DateField(help_text="Введите дата окончания акции", verbose_name="Дата окончания акции")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите продукт", verbose_name="Продукт")

    class Meta:
        ordering = ["-date_end"]
        verbose_name_plural = "Скидки"

    def __str__(self):
        return '%s %s - %s' % (self.product.name, self.date_start, self.date_end)

    @property
    def is_overdue(self):
        if self.date_end and date.today() > self.date_end:
            return True
        return False


class ImageProduct(models.Model):
    image = models.ImageField(upload_to='images/products/%Y/%m/%d/', help_text="Загрузите изображение продукта",
                              verbose_name="Изображение продукта")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите продукт", verbose_name="Продукт")

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = "store_image_product"
        verbose_name_plural = "Изображения продуктов"


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Выберите пользователя",
                             verbose_name="Пользователь")
    patronymic = models.CharField(max_length=64, help_text="Введите отчество", verbose_name="Отчество", null=True,
                                  blank=True)
    telephone = models.CharField(max_length=11, null=True, blank=True, help_text="Введите номер телефона",
                                 verbose_name="Номер телефон")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Введите дату рождения",
                                     verbose_name="Дата рождения")
    country = models.CharField(max_length=64, null=True, blank=True, help_text="Введите страну",
                               verbose_name="Страна")
    region = models.CharField(max_length=64, null=True, blank=True, help_text="Введите регион",
                              verbose_name="Регион")
    city = models.CharField(max_length=64, null=True, blank=True, help_text="Введите город",
                            verbose_name="Город")
    address = models.CharField(max_length=64, null=True, blank=True, help_text="Введите адрес",
                               verbose_name="Адрес")
    avatar = models.ImageField(upload_to='images/avatars/%Y/%m/%d/', help_text="Загрузите изображение",
                               verbose_name="Аватар пользователя", null=True, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = "user_info"
        verbose_name_plural = "Пользователи"


class Bonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Выберите пользователя",
                             verbose_name="Пользователь")
    quantity = models.PositiveIntegerField(help_text="Введите количество бонусов", verbose_name="Количество бонусов")
    date_start = models.DateField(help_text="Введите дату начала", verbose_name="Дата начала")
    date_end = models.DateField(help_text="Введите дату окончания", verbose_name="Дата окончания")

    class Meta:
        ordering = ["date_end"]
        verbose_name_plural = "Бонусы"

    def __str__(self):
        return '%s %d %s - %s' % (self.user.email, self.quantity, self.date_start, self.date_end)

    @property
    def is_overdue(self):
        if self.date_end and date.today() > self.date_end:
            return True
        return False


class Order(models.Model):
    order_date = models.DateField(help_text="Введите дату заказа", verbose_name="Дата заказа")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, help_text="Выберите пользователя",
                             verbose_name="Пользователь", null=True)

    class Meta:
        ordering = ["order_date"]
        verbose_name_plural = "Заказы пользователей"

    def __str__(self):
        return '%s: order - %d %s' % (self.user.email, self.id, self.order_date)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, help_text="Выберите продукт",
                                verbose_name="Продукт", null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text="Выберите заказ",
                              verbose_name="Заказ")
    quantity = models.PositiveIntegerField(help_text="Введите количество товара", verbose_name="Количество товара")

    def __str__(self):
        return '%s %s %d' % (self.product.name, self.order, self.quantity)

    class Meta:
        db_table = "store_order_product"
        verbose_name_plural = "Информация о заказе"


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите товар",
                                verbose_name="Товар")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Выберите пользователя",
                             verbose_name="Пользователь")

    class Meta:
        verbose_name_plural = "Корзины пользователей"

    def __str__(self):
        return '%s %s' % (self.user.email, self.product.name)


class Favourites(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите товар",
                                verbose_name="Избранный товар")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Выберите пользователя",
                             verbose_name="Пользователь")

    class Meta:
        verbose_name_plural = "Избранные товары пользователей"

    def __str__(self):
        return '%s %s' % (self.user.email, self.product.name)