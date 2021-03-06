# Generated by Django 3.0.5 on 2020-07-12 15:30

from django.db import migrations
import partial_date.fields


class Migration(migrations.Migration):

    dependencies = [
        ('staff_profile', '0005_projects_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='end_date',
            field=partial_date.fields.PartialDateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='start_date',
            field=partial_date.fields.PartialDateField(blank=True, null=True),
        ),
    ]
