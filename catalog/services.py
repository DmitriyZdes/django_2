from django.core.cache import cache

from config1.settings import CACHE_ENABLED
from catalog.models import Category


def get_category_list_from_cache():

    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(categories)
    return categories
