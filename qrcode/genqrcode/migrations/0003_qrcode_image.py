# Generated by Django 4.1.1 on 2023-02-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("genqrcode", "0002_alter_qrcode_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="qrcode",
            name="image",
            field=models.ImageField(
                default="images/None/no-img.jpg", upload_to="images/"
            ),
        ),
    ]
