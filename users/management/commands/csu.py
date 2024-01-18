from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(
            email='dfaerd@mail.ru',
            first_name='Dmitros',
            last_name='Dmitrosov',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('54321')
        user.save()
