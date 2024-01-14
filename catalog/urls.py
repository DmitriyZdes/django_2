from django.urls import path
from catalog.views import ProductDetailView, ProductListView, ProductCreateView, ProductDeleteView, ProductUpdateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('product_list', ProductListView.as_view(), name='pr_list'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('update/<int:pk>', ProductUpdateView.as_view, name='update_product'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
