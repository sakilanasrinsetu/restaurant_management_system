# Generated by Django 3.1.4 on 2021-01-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0071_auto_20210124_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentCompanyPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('promo_type', models.CharField(choices=[('PERCENTAGE', 'percentage'), ('AMOUNT', 'amount')], max_length=50)),
                ('max_amount', models.FloatField(default=0)),
                ('minimum_purchase_amount', models.FloatField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ManyToManyField(to='restaurant.Restaurant')),
            ],
        ),
    ]