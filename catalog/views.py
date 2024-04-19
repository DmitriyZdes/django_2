#from django.shortcuts import render
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, \
    UserPassesTestMixin
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# FBV контроллеры

#def home(request):

    #return render(request, 'catalog/home.html')

#def contacts(request):

    #if request.method == "POST":
        #name = request.POST.get("name")
        #number = request.POST.get("number")
        #message = request.POST.get("message")
        #print(f'{name}, {number}, {message}')
    #return render(request, 'catalog/contacts.html')


#def products_view(request):

    #products = Product.objects.all()
    #context = {
        #"title": 'Продукт',
        #"object_list": products
    #}
   # return render(request, 'products/product_list.html', context)


#def product(request, pk):

    #context = {
        #'title': 'Карточка товара',
        #'object_list': Product.objects.get(category_id=pk)
     #}

    #return render(request, 'products/product_detail.html', context)


# CBV контроллеры

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
    success_url = reverse_lazy("catalog:pr_list")

    def form_valid(self, form):
        new_product = form.save()
        new_product.save()
        version = Version.objects.create(product=new_product)
        version.ver_name = "created"
        version.save()
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:pr_list")

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def test_func(self):
        return self.request.user.is_superuser


    def get_context_data(self, **kwards):
        context_data = super().get_context_data(**kwards)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
