# Generated by Django 4.0.1 on 2022-05-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_category_favorite_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='off_url',
            field=models.URLField(max_length=150, unique=True),
        ),
    ]