from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    social_links = models.URLField(blank=True)

    def __str__(self):
        return self.name
