# Generated by Django 5.1.1 on 2024-09-14 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_rating',
        ),
    ]
