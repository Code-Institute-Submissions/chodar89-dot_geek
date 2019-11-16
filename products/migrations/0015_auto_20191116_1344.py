# Generated by Django 2.2.6 on 2019-11-16 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20191116_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_l',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_m',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_xl',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_xs',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_xxl',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_xxxl',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)]),
        ),
    ]