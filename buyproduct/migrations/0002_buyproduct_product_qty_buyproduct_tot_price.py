# Generated by Django 4.0 on 2022-02-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyproduct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyproduct',
            name='product_qty',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyproduct',
            name='tot_price',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]