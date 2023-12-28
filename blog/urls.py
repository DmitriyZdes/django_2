from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='art_list'),
    path('display/<slug:slug>', BlogDetailView.as_view(), name='art_detail'),
    path('create/', BlogCreateView.as_view(), name='art_create'),
    path('update/<slug:slug>', BlogUpdateView.as_view(), name='art_update'),
    path('delete/<slug:slug>', BlogDeleteView.as_view(), name='art_delete'),

]


