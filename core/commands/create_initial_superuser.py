import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    """
    Creates a superuser if one does not already exist.
    Reads username, email, and password from environment variables:
    DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
    """
    help = 'Creates a superuser non-interactively if one does not exist.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not all([username, email, password]):
            raise CommandError(
                "Missing environment variables: DJANGO_SUPERUSER_USERNAME, "
                "DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD"
            )

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.SUCCESS(f"Superuser with email '{email}' already exists. Skipping."))
            return

        self.stdout.write(f"Creating superuser '{username}' with email '{email}'...")
        User.objects.create_superuser(email=email, password=password, name=username)
        self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
