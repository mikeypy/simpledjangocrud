# Generated by Django 2.1.2 on 2018-10-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='quantity',
            field=models.IntegerField(max_length=500),
        ),
    ]
