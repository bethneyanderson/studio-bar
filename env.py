import os

os.environ.setdefault(
    'SECRET_KEY',
    'django-insecure-e8syowf6f815v%yxjk78=18f&zoe=a7!w-xc=%!vh^)bkpp&cy')

os.environ.setdefault(
    'DATABASE_URL',
    'postgresql://neondb_owner:npg_9zjNdUFYvi2Z@ep-lingering-night-a2q2afdh.eu-central-1.aws.neon.tech/dart_dry_smirk_228448')

os.environ.setdefault('DEBUG', 'True')

# Default password for staff accounts (used by create_staff command)
# Change this in production or set STAFF_DEFAULT_PASSWORD environment variable
os.environ.setdefault('STAFF_DEFAULT_PASSWORD', 'TempPassword123!')
