from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=30, default='open')

    def __str__(self):
        return self.title