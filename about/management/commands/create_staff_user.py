from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create staff users for managing content'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the staff user')
        parser.add_argument('--email', type=str, help='Email for the staff user')
        parser.add_argument(
            '--password',
            type=str,
            default='staffpass123',
            help='Password for the staff user')

    def handle(self, *args, **options):
        username = options['username']
        email = options.get('email', f'{username}@studio-bar.com')
        password = options['password']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User "{username}" already exists')
            )
            return

        # Create staff user
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created staff user "{username}" with password "{password}"'))
