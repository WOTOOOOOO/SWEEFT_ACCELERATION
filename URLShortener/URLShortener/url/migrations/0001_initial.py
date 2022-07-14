# Generated by Django 4.0.6 on 2022-07-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=15, unique=True)),
                ('count', models.IntegerField(max_length=20)),
            ],
        ),
    ]
