# Generated by Django 4.1.5 on 2023-02-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Styling",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company", models.CharField(max_length=150)),
                ("name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=150)),
                ("city", models.CharField(max_length=150)),
                ("state", models.CharField(max_length=150)),
                ("country", models.CharField(max_length=150)),
                ("purp", models.TextField(max_length=200)),
                ("file", models.FileField(upload_to="")),
            ],
        ),
    ]