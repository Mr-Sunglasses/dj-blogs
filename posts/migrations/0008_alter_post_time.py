# Generated by Django 4.2 on 2023-04-22 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 22, 9, 43, 28, 601277, tzinfo=datetime.timezone.utc)),
        ),
    ]