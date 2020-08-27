from django.db import models

# Create your models here.


class BackgroundImages(models.Model):
    img_url = models.FileField(upload_to='pics')
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Background Images'


