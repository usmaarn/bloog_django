# Generated by Django 5.0.4 on 2024-04-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0007_alter_post_options_rename_created_at_post_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
