# Generated by Django 3.0.5 on 2020-07-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_Hepeps', models.TextField()),
                ('our_img', models.FileField(upload_to='pics')),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Corevalues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_values', models.CharField(max_length=200)),
                ('img_core_value', models.FileField(upload_to='pics')),
                ('status', models.BooleanField()),
                ('core_values_details', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Our Core Values',
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.CharField(max_length=200)),
                ('img_mission', models.FileField(upload_to='pics')),
                ('status', models.BooleanField()),
                ('mission_details', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Mission',
            },
        ),
        migrations.CreateModel(
            name='Ourstory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('our_story', models.TextField()),
                ('img_our_story', models.FileField(upload_to='pics')),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Our Story',
            },
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', models.CharField(max_length=200)),
                ('img_vision', models.FileField(upload_to='pics')),
                ('status', models.BooleanField()),
                ('vision_details', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Vision',
            },
        ),
    ]
