from django.urls import path
from catalog.views import ProductDetailView, ProductListView #product, products_view #home, contacts,
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', home, name='home'),
    #path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view()), #product),
    path('product_list',ProductListView.as_view() #products_view
)]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
