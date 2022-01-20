from django.db import models
from model_utils.models import TimeStampedModel


class Person(TimeStampedModel):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
