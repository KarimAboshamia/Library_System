# Generated by Django 3.2.4 on 2021-07-15 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryPages', '0004_auto_20210714_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='counter',
            field=models.IntegerField(default=1),
        ),
    ]
