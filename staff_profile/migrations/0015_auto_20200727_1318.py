# Generated by Django 3.0.5 on 2020-07-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_profile', '0014_certifications_institution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='training_description',
        ),
        migrations.AddField(
            model_name='training',
            name='description',
            field=models.CharField(default='desc', max_length=1500),
            preserve_default=False,
        ),
    ]
