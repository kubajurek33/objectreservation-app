# Generated by Django 4.2.6 on 2023-10-22 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_reservation_res_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='res_price',
            new_name='price',
        ),
    ]
