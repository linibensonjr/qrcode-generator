# Generated by Django 4.1.1 on 2022-09-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("genqrcode", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qrcode",
            name="text",
            field=models.TextField(help_text="Enter text to generate"),
        ),
    ]
