# Generated by Django 3.0.5 on 2020-04-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburgers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hamburger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=512)),
                ('image', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.CharField(default=None, max_length=512),
            preserve_default=False,
        ),
    ]
