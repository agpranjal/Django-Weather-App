# Generated by Django 3.0.3 on 2020-03-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='city',
            name='country_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
