# Generated by Django 3.0.5 on 2020-06-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20200620_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]