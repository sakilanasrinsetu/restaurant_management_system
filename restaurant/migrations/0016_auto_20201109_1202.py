# Generated by Django 3.1.1 on 2020-11-09 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_auto_20201108_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordereditem',
            old_name='amount',
            new_name='quantity',
        ),
    ]