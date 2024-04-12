from django.db import models
import random

class Woman(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    story = models.TextField(default="")

    def random_story():
        stories = [
            "She overcame challenges and built her own successful business.",
            "She dedicated her life to empowering other women in her community.",
            "She fought for gender equality and made significant changes in her society.",
            "She pursued her passion and became a leader in her field.",
            "She inspired others with her resilience and determination."
        ]
        return random.choice(stories)

    random_story = staticmethod(random_story)

    def save(self, *args, **kwargs):
        if not self.story:
            self.story = self.random_story()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
