from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=200)
    service_desc = models.TextField()
    service_img = models.FileField(upload_to='pics')
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Services'