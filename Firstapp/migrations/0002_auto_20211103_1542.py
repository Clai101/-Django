# Generated by Django 3.1.6 on 2021-11-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='for_anonym_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
    ]
