# Generated by Django 4.1.3 on 2022-11-16 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_order_trans_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
    ]
