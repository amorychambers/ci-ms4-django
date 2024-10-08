# Generated by Django 5.1.1 on 2024-09-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
