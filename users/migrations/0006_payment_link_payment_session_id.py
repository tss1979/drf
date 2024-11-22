# Generated by Django 5.1.2 on 2024-11-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id сессии'),
        ),
    ]