# Generated by Django 3.1.4 on 2021-07-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0088_restaurant_sd_charge_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='hide_sell_report',
            field=models.CharField(choices=[('HIGHEST_PRICE', 'Highest Price'), ('LOWEST_PRICE', 'Lowest Price'), ('FOOD_ORDER', 'Food Order')], default='FOOD_ORDER', max_length=50),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='hide_sell_report_is_percentage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='number_of_report_hide',
            field=models.IntegerField(default=0),
        ),
    ]