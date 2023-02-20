from django.db import models

# Create your models here.
class QRCode(models.Model):
    text = models.TextField(null=False, help_text="Enter text to generate")
    qr_name = models.TextField(null=False, help_text="Enter qrcode name")
   
    def __str__(self):
        return self.qr_name