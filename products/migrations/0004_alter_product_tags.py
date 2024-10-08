# Generated by Django 5.1.1 on 2024-09-13 14:24

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('coffee', 'Coffee'), ('equipment', 'Equipment'), ('single', 'Single Origin'), ('blend', 'Blend'), ('sale', 'Sale'), ('bundle', 'Bundle')], max_length=41),
        ),
    ]
