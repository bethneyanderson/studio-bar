from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    social_links = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    venue_name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='events')
    image = models.ImageField(upload_to='events/', blank=True, null=True, help_text='Event poster or promotional image')

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%Y-%m-%d')})"