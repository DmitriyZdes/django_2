from django.urls import reverse_lazy

from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.utils.text import slugify


# CBV

class BlogListView(ListView):

    model = Blog
    extra_context = {
        'title': 'Блоги'
    }
    template_name = 'blog/blog_list'

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blog/blog_detail'

    def get_object(self, queryset=None):

        obj = super().get_object(queryset)
        obj.count_view += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):

    model = Blog
    fields = ('title', 'slug' , 'is_published', 'content', 'image', 'creation_date', 'count_view')
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_form'

    def form_valid(self, form):

        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):

    model = Blog
    fields = ('title', 'is_published', 'content', 'image')
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_form'

    def form_valid(self, form):

        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):

    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_confirm_delete'

