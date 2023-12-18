from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        category_list = [
            {'name': "Cпорттовары", 'description': "Для здорового образа жизни"},
            {'name': "Канцелярия", 'description': "Всегда актуальны"}

        ]

        created_list = []
        for category in category_list:
            created_list.append(Category(**category))

        Category.objects.bulk_create(created_list)
