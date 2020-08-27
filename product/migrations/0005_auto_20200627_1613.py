# Generated by Django 3.0.5 on 2020-06-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200627_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='logo',
        ),
        migrations.AddField(
            model_name='order',
            name='postal_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('purchased', 'Purchased'), ('cancelled', 'Cancelled')], default='ordered', max_length=50),
        ),
    ]
