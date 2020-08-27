from django.db import models
from partial_date import PartialDateField


class Role(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_names = models.CharField(max_length=200, null=True, blank=True)
    img_url = models.FileField(upload_to='staff')
    bio = models.TextField(max_length=5000)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    display_order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Hepeps Team'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def education(self):
        return Education.objects.filter(team=self, publish=True)

    @property
    def experiences(self):
        return Experience.objects.filter(team=self, publish=True)

    @property
    def certificates(self):
        return Certifications.objects.filter(team=self, publish=True)

    @property
    def trainings(self):
        return Training.objects.filter(team=self, publish=True)

    @property
    def projects(self):
        return Projects.objects.filter(team=self, publish=True)

    @property
    def publications(self):
        return Publication.objects.filter(team=self, publish=True)


class Country(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Country'

    def __str__(self):
        return self.name


class Education(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    program = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    school_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True, blank=True)
    start_date = PartialDateField()
    end_date = PartialDateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    publish = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.program


class Experience(models.Model):
    team = models.ForeignKey(Team, default=1, verbose_name="team_member_ID",
                             on_delete=models.CASCADE)
    position = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    company_name = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, null=True, blank=True)
    start_date = PartialDateField()
    end_date = PartialDateField(null=True, blank=True)
    publish = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Work Experience'


class Certifications(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    cert_name = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    institution = models.CharField(max_length=250)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    publish = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Certification'


class Training(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    training_cert = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    training_company = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    publish = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Training'


class Projects(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    company_name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    method_used = models.TextField(max_length=1200)
    role_on_project = models.CharField(max_length=150)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    tools_used = models.TextField(max_length=2500, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    publish = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Projects Managed'


class Publication(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    description = models.TextField(max_length=2500)
    reference_link = models.URLField(max_length=256)
    publish = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Publication'
