# Generated by Django 5.0.6 on 2024-06-17 21:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tweet", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tweet",
            old_name="creaTed_at",
            new_name="created_at",
        ),
    ]
