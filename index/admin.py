from django.contrib import admin
from .models import Artist, Event
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'social_links')  # These match your Artist model
    search_fields = ('name', 'genre')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue_name', 'artist')
    search_fields = ('title', 'venue_name')
    list_filter = ('date', 'artist')


