# Generated by Django 3.0.5 on 2020-04-19 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburgers', '0002_auto_20200419_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamburger',
            name='ingredients',
            field=models.ManyToManyField(to='hamburgers.Ingredient'),
        ),
    ]
