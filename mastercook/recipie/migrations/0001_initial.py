# Generated by Django 4.2.5 on 2023-09-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
                ('image_url', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('preparation', models.TextField()),
                ('image_url', models.URLField(max_length=2083)),
            ],
        ),
    ]
