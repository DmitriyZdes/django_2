from django.urls import path
from catalog.views import product, products_view #home, contacts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', home, name='home'),
    #path('contacts/', contacts, name='contacts'),
    path('product_list/<int:pk>/', product, name='product_list'),
    path('product_inf', products_view, name='product_inf')] #static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
