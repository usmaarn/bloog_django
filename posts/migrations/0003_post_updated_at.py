# Generated by Django 5.0.4 on 2024-04-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_post_banner"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
