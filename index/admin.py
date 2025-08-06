from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue_name', 'artist', 'get_price_display')
    search_fields = ('title', 'venue_name')
    list_filter = ('date', 'artist', 'price')
    readonly_fields = ('image_preview',)
    fields = ('title', 'date', 'description', 'venue_name', 'artist', 'price', 'image', 'image_preview')
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px;">'
        return "No image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


