# Generated by Django 3.0.5 on 2020-06-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200627_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='order_status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('purchased', 'Purchased'), ('cancelled', 'Cancelled')], default='ordered', max_length=50),
            preserve_default=False,
        ),
    ]
