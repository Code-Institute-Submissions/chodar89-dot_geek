# Generated by Django 3.0 on 2019-12-07 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]