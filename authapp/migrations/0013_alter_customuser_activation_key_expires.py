# Generated by Django 3.2.13 on 2022-06-30 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_alter_customuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 15, 36, 31, 371101, tzinfo=utc)),
        ),
    ]
