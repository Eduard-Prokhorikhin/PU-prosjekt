# Generated by Django 4.1.6 on 2023-02-09 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0006_alter_post_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="image_url", new_name="image",
        ),
    ]