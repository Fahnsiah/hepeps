# Generated by Django 3.0.5 on 2020-07-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_profile', '0019_auto_20200727_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='method_used',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateField(),
        ),
    ]
