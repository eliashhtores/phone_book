from django.db import models
from model_utils.models import TimeStampedModel
from .managers import ReunionManager


class Hobby(TimeStampedModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.name


class Person(TimeStampedModel):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    notes = models.TextField(blank=True)
    hobbies = models.ManyToManyField(Hobby, blank=True)

    def __str__(self):
        return self.name


class Reunion(TimeStampedModel):
    subject = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    objects = ReunionManager()

    def __str__(self):
        return self.subject
