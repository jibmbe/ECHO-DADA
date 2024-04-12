from django.db import models


class EnvironmentalProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.title
