# Generated by Django 4.2.4 on 2023-08-10 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_failedloginattempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='last_login',
        ),
        migrations.AddField(
            model_name='customer',
            name='last_login_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]