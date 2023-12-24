#from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView

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
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):

    model = Product

    template_name = 'products/product_detail.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


