# Generated by Django 2.1.2 on 2018-10-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0009_auto_20181008_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
