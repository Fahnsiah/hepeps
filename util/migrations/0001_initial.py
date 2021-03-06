# Generated by Django 3.0.5 on 2020-07-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('sender', models.CharField(max_length=100)),
                ('fail_silently', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
