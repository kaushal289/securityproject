# Generated by Django 4.0 on 2022-02-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyproduct', '0003_buyproduct_esewa_id_buyproduct_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyproduct',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
