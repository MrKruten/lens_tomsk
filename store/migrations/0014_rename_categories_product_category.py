# Generated by Django 4.0.3 on 2022-10-27 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_category_subcategory_remove_product_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]
