# Generated by Django 4.1.2 on 2022-12-04 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='totalPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
