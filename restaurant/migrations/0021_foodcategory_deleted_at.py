# Generated by Django 3.1.1 on 2020-11-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0020_auto_20201112_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcategory',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]