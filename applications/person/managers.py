from django.db import models
from django.db.models import Count


class ReunionManager(models.Manager):

    def get_reunion_job(self):
        return self.values('person__job_title').annotate(Count('person__job_title'))
