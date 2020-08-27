from django.db import models


# Create your models here.
class About(models.Model):
    about_Hepeps = models.TextField()
    #history = models.TextField()
    our_img = models.FileField(upload_to='pics')
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'About'


class Ourstory(models.Model):
    our_story = models.TextField()
    img_our_story = models.FileField(upload_to='pics')
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Our Story'


class Vision(models.Model):
    vision = models.CharField(max_length=200)
    img_vision = models.FileField(upload_to='pics')
    status = models.BooleanField()
    vision_details=models.TextField(null=True)

    class Meta: verbose_name_plural = 'Vision'


class Mission(models.Model):
    mission = models.CharField(max_length=200)
    img_mission = models.FileField(upload_to='pics')
    status = models.BooleanField()
    mission_details = models.TextField(null=True)

    class Meta: verbose_name_plural = 'Mission'


class Corevalues(models.Model):
    core_values = models.CharField(max_length=200)
    img_core_value = models.FileField(upload_to='pics')
    status = models.BooleanField()
    core_values_details = models.TextField(null=True)

    class Meta: verbose_name_plural = 'Our Core Values'
