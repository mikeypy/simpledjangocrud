# Generated by Django 2.1.2 on 2018-10-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0006_auto_20181008_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='name',
            field=models.CharField(help_text='Laptop Name', max_length=120),
        ),
    ]
