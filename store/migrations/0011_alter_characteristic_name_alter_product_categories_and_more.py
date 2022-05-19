# Generated by Django 4.0.3 on 2022-05-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_categories_alter_product_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristic',
            name='name',
            field=models.TextField(help_text='Введите название характеристики', verbose_name='Название характеристики'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, help_text='Выберите категории', null=True, to='store.category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.ManyToManyField(blank=True, help_text='Выберите скидку', null=True, to='store.discount', verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='options',
            field=models.ManyToManyField(blank=True, help_text='Выберите опции', null=True, to='store.option', verbose_name='Опции'),
        ),
    ]