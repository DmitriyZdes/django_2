from django.urls import path
from django.conf.urls.static import static
from catalog.views import home, contacts, product
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product')] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
