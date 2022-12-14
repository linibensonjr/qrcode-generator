# Generated by Django 4.1.1 on 2022-09-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QRCode",
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
                ("text", models.IntegerField(help_text="Enter text to generate")),
                ("qr_name", models.TextField(help_text="Enter qrcode name")),
            ],
        ),
    ]
