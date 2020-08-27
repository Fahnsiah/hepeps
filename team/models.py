from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_names = models.CharField(max_length=200, null=True, blank=True)
    img_url = models.FileField(upload_to='team')
    Bio = models.TextField(max_length=5000)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    display_order = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Hepeps Team'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

