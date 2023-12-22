from django.urls import path
from catalog.views import product, products_view #home, contacts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', home, name='home'),
    #path('contacts/', contacts, name='contacts'),
    path('product_list/<int:pk>/', product),
    path('product_inf', products_view)]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
