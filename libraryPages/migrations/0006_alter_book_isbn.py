# Generated by Django 3.2.4 on 2021-07-15 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryPages', '0005_book_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=13),
        ),
    ]
