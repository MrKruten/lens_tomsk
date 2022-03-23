from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Manufacture(models.Model):
    name = models.CharField(max_length=64, help_text="Введите название компании", verbose_name="Название компании")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, help_text="Введите название категории", verbose_name="Название категории")
    image = models.ImageField(upload_to='images/categories/% Y/% m/% d/', help_text="Загрузите изображение",
                              verbose_name="Изображение категории", null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, help_text="Введите название продукта", verbose_name="Название продукта")
    price = models.DecimalField(max_digits=15, decimal_places=4, help_text="Введите цену", verbose_name="Цена продукта")
    description = models.TextField(help_text="Введите описание", verbose_name="Описание продукта")
    quantity = models.PositiveIntegerField(help_text="Введите количество продукта", verbose_name="Описание продукта")
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, help_text="Выберите компанию",
                                    verbose_name="Компания")
    categories = models.ManyToManyField(Category, help_text="Выберите категорию", verbose_name="Категория")

    class Meta:
        ordering = ["price", "quantity"]

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    name = models.TextField(help_text="Введите название характеристики", verbose_name="Название категории")
    description = models.TextField(help_text="Введите описание характеристики", verbose_name="Описание характеристики")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите продукт", verbose_name="Продукт")

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.TextField(help_text="Введите название опции", verbose_name="Название опции")
    description = models.TextField(help_text="Введите описание опции", verbose_name="Описание опции")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите продукт", verbose_name="Продукт")

    def __str__(self):
        return self.name


class Discount(models.Model):
    percentage = models.DecimalField(max_digits=10, decimal_places=2, help_text="Введите процент скидки",
                                     verbose_name="Процент скидки")
    date_start = models.DateField(help_text="Введите дату начала акции", verbose_name="Дата начала акции")
    date_end = models.DateField(help_text="Введите дата окончания акции", verbose_name="Дата окончания акции")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите продукт", verbose_name="Продукт")

    class Meta:
        ordering = ["-date_end"]

    def __str__(self):
        return '%s %s - %s' % (self.product, self.date_start, self.date_end)

    @property
    def is_overdue(self):
        if self.date_end and date.today() > self.date_end:
            return True
        return False


class ImageProduct(models.Model):
    image = models.ImageField(upload_to='images/products/% Y/% m/% d/', help_text="Загрузите изображение продукта",
                              verbose_name="Изображение продукта")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите продукт", verbose_name="Продукт")

    def __str__(self):
        return self.product

    class Meta:
        db_table = "store_image_product"


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
    avatar = models.ImageField(upload_to='images/avatars/% Y/% m/% d/', help_text="Загрузите изображение",
                               verbose_name="Аватар пользователя", null=True, blank=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = "user_info"


class Bonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Выберите пользователя",
                             verbose_name="Пользователь")
    quantity = models.PositiveIntegerField(help_text="Введите количество бонусов", verbose_name="Количество бонусов")
    date_start = models.DateField(help_text="Введите дату начала", verbose_name="Дата начала")
    date_end = models.DateField(help_text="Введите дату окончания", verbose_name="Дата окончания")

    class Meta:
        ordering = ["date_end"]

    def __str__(self):
        return '%s %d %s - %s' % (self.user, self.quantity, self.date_start, self.date_end)

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

    def __str__(self):
        return '%s: order - %d %s' % (self.user, self.id, self.order_date)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, help_text="Выберите продукт",
                                verbose_name="Продукт", null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text="Выберите заказ",
                              verbose_name="Заказ")
    quantity = models.PositiveIntegerField(help_text="Введите количество товара", verbose_name="Количество товара")

    def __str__(self):
        return '%s %s %d' % (self.product, self.order, self.quantity)

    class Meta:
        db_table = "store_order_product"


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Выберите товар",
                                verbose_name="Товар")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Выберите пользователя",
                             verbose_name="Пользователь")

    def __str__(self):
        return '%s %s' % (self.user, self.product)
