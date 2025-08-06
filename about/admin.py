from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'updated_at', 'updated_by']
    readonly_fields = ['updated_at', 'updated_by']

    fieldsets = (
        ('Story Section', {
            'fields': ('story_title', 'story_lead', 'story_content')
        }),
        ('Mission Section', {
            'fields': ('mission_title', 'mission_content')
        }),
        ('Space Section', {
            'fields': ('space_title', 'space_content')
        }),
        ('Programming Section', {
            'fields': ('programming_title', 'programming_content')
        }),
        ('Community Section', {
            'fields': ('community_title', 'community_content')
        }),
        ('Contact Information', {
            'fields': ('address', 'opening_hours', 'email')
        }),
        ('Metadata', {
            'fields': ('updated_at', 'updated_by'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
