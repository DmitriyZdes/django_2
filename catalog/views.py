from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from catalog.models import Product, Version, Category
from catalog.forms import ProductForm, VersionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.services import get_category_list_from_cache


class ProductListView(ListView):

    model = Product
    extra_context = {
        "title": 'Продукт',
        'object_list': Product.objects.all()
    }
    form_class = ProductForm


class ProductDetailView(DetailView):

    model = Product
    form_class = ProductForm

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        new_product = form.save()
        new_product.save()
        version = Version.objects.create(product=new_product)
        version.ver_name = "created"
        version.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def test_func(self):
        return self.request.user.is_superuser

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404

    def get_context_data(self, **kwards):
        context_data = super().get_context_data(**kwards)
        productformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = productformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = productformset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class CategoryListView(ListView):

    model = Category

    def get_queryset(self):

        return get_category_list_from_cache()
