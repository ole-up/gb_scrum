# Generated by Django 3.2.13 on 2022-06-18 15:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_customuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 15, 49, 31, 770896, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users_avatars'),
        ),
        migrations.AlterField(
            model_name='customuserprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'М'), ('F', 'Ж')], max_length=1, verbose_name='пол'),
        ),
    ]
