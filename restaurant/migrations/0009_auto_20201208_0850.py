# Generated by Django 3.1.2 on 2020-12-08 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_restaurant_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='cover_img',
            field=models.ImageField(upload_to='images/restaurant/cover'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
