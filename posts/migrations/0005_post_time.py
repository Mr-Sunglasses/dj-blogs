# Generated by Django 4.2 on 2023-04-21 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_alter_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 21, 21, 31, 24, 592214)
            ),
        ),
    ]
