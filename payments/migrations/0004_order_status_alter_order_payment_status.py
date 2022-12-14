# Generated by Django 4.1.3 on 2022-11-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_remove_order_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('success', 'Success'), ('due', 'Due')], default='success', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('success', 'Success'), ('faild', 'Faild'), ('cancel', 'Cancel')], max_length=20, null=True),
        ),
    ]
