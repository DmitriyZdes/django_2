from django.urls import path
from catalog.views import product, products_view #home, contacts


urlpatterns = [
    #path('', home, name='home'),
    #path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),
    path('products_view', products_view, name='products_view')]
