# Generated by Django 3.1.4 on 2021-07-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0039_useraccount_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='browsing_as_ghost',
            field=models.BooleanField(default=False),
        ),
    ]
