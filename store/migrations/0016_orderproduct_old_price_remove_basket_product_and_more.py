# Generated by Django 4.0.3 on 2022-11-10 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0015_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='old_price',
            field=models.DecimalField(decimal_places=4, default=0, help_text='Введите цену', max_digits=15, verbose_name='Старая цена продукта'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='basket',
            name='product',
        ),
        migrations.AddField(
            model_name='basket',
            name='product',
            field=models.ManyToManyField(help_text='Выберите товар', to='store.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='user',
            field=models.ForeignKey(help_text='Выберите пользователя', on_delete=django.db.models.deletion.CASCADE, related_name='bonuses', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='product',
            field=models.ForeignKey(help_text='Выберите продукт', on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='store.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(help_text='Выберите пользователя', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(help_text='Выберите заказ', on_delete=django.db.models.deletion.CASCADE, related_name='products_in_order', to='store.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='store.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(help_text='Выберите пользователя', on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]