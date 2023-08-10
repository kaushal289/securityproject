# Generated by Django 4.2.4 on 2023-08-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedLoginAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('attempts', models.IntegerField(default=0)),
                ('last_attempt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
