# Generated by Django 4.0.3 on 2022-05-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_product_categories_alter_product_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_recommended',
            field=models.BooleanField(blank=True, default=False, help_text='Рекомендовать этот продукт', verbose_name='Рекомендовать?'),
        ),
    ]