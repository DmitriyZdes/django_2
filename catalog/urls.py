from django.urls import path
from catalog.views import product, products_view #home, contacts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', home, name='home'),
    #path('contacts/', contacts, name='contacts'),
    path('product_inf/<int:pk>/', product, name='product_inf'),
    path('product_list', products_view, name='product_list')] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
