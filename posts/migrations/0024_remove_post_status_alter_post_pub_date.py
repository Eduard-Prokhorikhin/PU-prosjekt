# Generated by Django 4.1.6 on 2023-03-21 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_alter_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(
                2023, 3, 21, 15, 19, 43, 350444), verbose_name='date published'),
        ),
    ]
