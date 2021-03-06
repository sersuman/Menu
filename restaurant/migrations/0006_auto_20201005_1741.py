# Generated by Django 3.1 on 2020-10-05 11:56

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20201005_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ManyToManyField(related_name='category_name', to='restaurant.Category'),
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Veg', 'Veg'), ('Non Veg', 'non_veg'), ('Chicken', 'chicken'), ('Mutton', 'mutton'), ('Buff', 'buff'), ('Pork', 'pork')], max_length=36),
        ),
    ]
