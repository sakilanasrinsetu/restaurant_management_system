# Generated by Django 3.1.1 on 2021-02-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0073_foodorder_applied_promo_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='versionupdate',
            name='build_number',
            field=models.IntegerField(default=0),
        ),
    ]