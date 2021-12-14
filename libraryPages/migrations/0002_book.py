# Generated by Django 3.2.4 on 2021-07-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryPages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('publication_year', models.CharField(max_length=4)),
                ('author_name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Fiction', 'Fiction'), ('Sceince', 'Sceince'), ('Stories', 'Stories')], max_length=50)),
            ],
        ),
    ]