# Generated by Django 4.0.3 on 2022-10-27 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_options_product_option_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]