# Generated by Django 4.2.4 on 2023-08-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradmin',
            name='password',
            field=models.CharField(default='admin', max_length=128),
        ),
    ]
