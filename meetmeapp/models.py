from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Meeting(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
