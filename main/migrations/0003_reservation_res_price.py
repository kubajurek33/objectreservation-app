# Generated by Django 4.2.6 on 2023-10-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pricelist_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='res_price',
            field=models.FloatField(null=True),
        ),
    ]
