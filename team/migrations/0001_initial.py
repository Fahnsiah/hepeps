# Generated by Django 3.0.5 on 2020-06-20 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('other_names', models.CharField(blank=True, max_length=200, null=True)),
                ('img_url', models.FileField(upload_to='pics')),
                ('Bio', models.TextField()),
                ('is_active', models.BooleanField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Role')),
            ],
            options={
                'verbose_name_plural': 'Hepeps Team',
            },
        ),
    ]
