from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create or update the default admin account.'

    def handle(self, *args, **options):
        username = 'abc123'
        password = 'abc123'
        email = 'abc123@example.com'

        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            },
        )

        if not created:
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
            user.email = email

        user.set_password(password)
        user.save()

        action = 'created' if created else 'updated'
        self.stdout.write(self.style.SUCCESS(f'Default admin account {action}: {username}/{password}'))