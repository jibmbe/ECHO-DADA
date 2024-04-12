from django.db import models


class CleanupActivity(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    

    def __str__(self):
        return self.location
