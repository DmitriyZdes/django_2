from django.urls import path
from django.conf.urls.static import static
from catalog.views import home, contacts
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
