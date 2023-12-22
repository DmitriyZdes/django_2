from django.urls import path
from catalog.views import product, products_view #home, contacts


urlpatterns = [
    #path('', home, name='home'),
    #path('contacts/', contacts, name='contacts'),
    path('product_inf/<int:pk>/', product, name='product_inf'),
    path('product_list', products_view, name='products_list')]
