# Generated by Django 5.1.4 on 2025-01-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_payment_amount_payment_order_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
