# Generated by Django 4.0.3 on 2022-03-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_imageproduct_table_alter_orderproduct_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='images/categories/%Y/%m/%d/', verbose_name='Изображение категории'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(help_text='Загрузите изображение продукта', upload_to='images/products/%Y/%m/%d/', verbose_name='Изображение продукта'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='images/avatars/%Y/%m/%d/', verbose_name='Аватар пользователя'),
        ),
    ]
