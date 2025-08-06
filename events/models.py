from django.db import models
from django.contrib.auth.models import User
from artists.models import Artist

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    venue_name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='events')
    image = models.ImageField(upload_to='events/', blank=True, null=True, help_text='Event poster or promotional image')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, help_text='Ticket price (0.00 for free events)')

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%Y-%m-%d')})"
    
    def get_price_display(self):
        """Return 'Free' if price is 0.00, otherwise return formatted price"""
        if self.price == 0:
            return 'Free'
        return f'£{self.price:.2f}'
