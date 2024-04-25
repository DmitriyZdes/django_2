from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductDetailView, ProductListView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView, CategoryListView
from django.conf.urls.static import static
from django.conf import settings
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('product_list', ProductListView.as_view(), name='pr_list'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('category_list', CategoryListView.as_view(), name='category_list'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
