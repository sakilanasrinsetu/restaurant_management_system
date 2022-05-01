# Generated by Django 3.1.4 on 2021-04-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0086_auto_20210419_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='remove_discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodorder',
            name='remove_discount_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodorder',
            name='remove_discount_amount_is_percentage',
            field=models.BooleanField(default=False),
        ),
    ]
