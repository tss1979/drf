# Generated by Django 5.1.2 on 2024-11-22 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_payment_link_payment_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 22, 20, 46, 50, 743007), verbose_name='дата оплаты'),
        ),
    ]
