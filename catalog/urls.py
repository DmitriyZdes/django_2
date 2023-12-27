from django.urls import path
from catalog.views import ProductDetailView, ProductListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('product_detail/<int:pk>/', ProductDetailView.as_view()),
    path('product_list',ProductListView.as_view(),
)] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
