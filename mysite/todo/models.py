import datetime

from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField()

    def was_recently_added(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title


class Todo(models.Model):
    content = models.CharField(max_length=300)
    todo = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
