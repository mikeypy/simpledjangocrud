# Generated by Django 2.1.2 on 2018-10-08 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0010_auto_20181008_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='name',
            field=models.CharField(help_text=' Enter a Laptop Name. E.g Acer', max_length=120),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='quantity',
            field=models.PositiveIntegerField(help_text=' Please Enter Quantity to store. Note Cannot exceed 500', validators=[django.core.validators.MaxValueValidator(500)]),
        ),
    ]
