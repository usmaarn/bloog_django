# Generated by Django 5.0.4 on 2024-04-22 16:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_bookmark"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
    ]
