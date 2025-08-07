import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create staff users'

    def handle(self, *args, **options):
        # Get password from environment variable or use a default for development
        default_password = os.environ.get('STAFF_DEFAULT_PASSWORD', 'TempPassword123!')
        
        # Create staff1
        if not User.objects.filter(username='staff1').exists():
            user1 = User.objects.create_user(
                username='staff1',
                email='staff1@studiobar.com',
                password=default_password,
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
                password=default_password,
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
            self.style.WARNING('Staff users created with default password.')
        )
        self.stdout.write(
            self.style.WARNING('Please change passwords after first login.')
        )
