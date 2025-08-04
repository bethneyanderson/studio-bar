from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create staff users'

    def handle(self, *args, **options):
        # Create staff1
        if not User.objects.filter(username='staff1').exists():
            user1 = User.objects.create_user(
                username='staff1',
                email='staff1@studiobar.com',
                password='StudioBar2025!',
                is_staff=True
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created staff user: {user1.username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('User staff1 already exists')
            )

        # Create staff2
        if not User.objects.filter(username='staff2').exists():
            user2 = User.objects.create_user(
                username='staff2',
                email='staff2@studiobar.com',
                password='StudioBar2025!',
                is_staff=True
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created staff user: {user2.username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('User staff2 already exists')
            )

        self.stdout.write(
            self.style.SUCCESS('Staff users setup complete!')
        )
        self.stdout.write(
            self.style.WARNING('Default password for both accounts: StudioBar2025!')
        )
        self.stdout.write(
            self.style.WARNING('Please change passwords after first login.')
        )
