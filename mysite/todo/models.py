import datetime

from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField()

    def was_recently_added(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
