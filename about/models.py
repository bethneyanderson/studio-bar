from django.db import models


class About(models.Model):
    """Model for About page content that can be edited by staff"""

    # Story Section
    story_title = models.CharField(max_length=200, default="Our Story")
    story_lead = models.TextField(help_text="Main paragraph for the story section")
    story_content = models.TextField(
        help_text="Additional content for the story section")

    # Mission Section
    mission_title = models.CharField(max_length=200, default="Our Mission")
    mission_content = models.TextField(help_text="Content for the mission section")

    # Space Section
    space_title = models.CharField(max_length=200, default="The Space")
    space_content = models.TextField(help_text="Content for the space section")

    # Programming Section
    programming_title = models.CharField(
        max_length=200, default="Programming & Production")
    programming_content = models.TextField(
        help_text="Content for the programming section")

    # Community Section
    community_title = models.CharField(
        max_length=200, default="Community & Partnerships")
    community_content = models.TextField(help_text="Content for the community section")

    # Contact Information
    address = models.TextField(default="71 Bread St\nPenzance TR18 2EQ")
    opening_hours = models.TextField(
        default="Monday – Thursday: 5pm – 12am\nFriday & Saturday: 5pm - 3am\nSunday: 3pm - 11pm")
    email = models.EmailField(default="info@studiobar.com")

    # Metadata
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return f"About Page (Last updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')})"

    def save(self, *args, **kwargs):
        # Ensure only one About instance exists
        if not self.pk and About.objects.exists():
            # If trying to create a new instance when one already exists, update the
            # existing one
            existing = About.objects.first()
            existing.story_title = self.story_title
            existing.story_lead = self.story_lead
            existing.story_content = self.story_content
            existing.mission_title = self.mission_title
            existing.mission_content = self.mission_content
            existing.space_title = self.space_title
            existing.space_content = self.space_content
            existing.programming_title = self.programming_title
            existing.programming_content = self.programming_content
            existing.community_title = self.community_title
            existing.community_content = self.community_content
            existing.address = self.address
            existing.opening_hours = self.opening_hours
            existing.email = self.email
            existing.updated_by = self.updated_by
            existing.save()
            return existing
        return super().save(*args, **kwargs)
