# Generated by Django 5.0.4 on 2024-04-22 12:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0003_alter_comment_options_alter_reply_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={},
        ),
        migrations.AlterModelOptions(
            name="reply",
            options={},
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="created_at",
            new_name="date",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="updated_at",
            new_name="modified",
        ),
        migrations.RenameField(
            model_name="reply",
            old_name="created_at",
            new_name="date",
        ),
        migrations.RenameField(
            model_name="reply",
            old_name="updated_at",
            new_name="modified",
        ),
    ]
