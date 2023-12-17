from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):

    def fill(self):

        Product.objects.all().delete()
        product_list = [
            {'name': 'яблоко', 'pk': 1, 'category': 'фрукты'},
            {'name': 'помидор', 'pk': 2, 'category': 'овощи'}

        ]

        created_list = []
        for product in product_list:
            created_list.append(Product(**product))

        Product.objects.bulk_create(created_list)
