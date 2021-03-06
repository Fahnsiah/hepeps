# Generated by Django 3.0.5 on 2020-07-27 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff_profile', '0008_auto_20200727_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
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
                ('is_active', models.BooleanField(default=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff_profile.Role')),
            ],
            options={
                'verbose_name_plural': 'Hepeps Team',
            },
        ),
        migrations.AlterField(
            model_name='certifications',
            name='team_member_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff_profile.Team', verbose_name='team_member_ID'),
        ),
        migrations.AlterField(
            model_name='education',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff_profile.Team', verbose_name='team_member_ID'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff_profile.Team', verbose_name='team_member_ID'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff_profile.Role', verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff_profile.Team', verbose_name='team_member_ID'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff_profile.Team', verbose_name='team_member_ID'),
        ),
        migrations.AlterField(
            model_name='training',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff_profile.Team', verbose_name='team_member_ID'),
        ),
    ]
