# Generated by Django 4.1.6 on 2023-02-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_remove_post_absoulte_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image_url",
            field=models.ImageField(default="", upload_to="productImages/"),
        ),
    ]
