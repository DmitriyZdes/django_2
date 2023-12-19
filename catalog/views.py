from django.shortcuts import render
from catalog.models import Product

def home(request):

    return render(request, 'catalog/home.html')


def contacts(request):

    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        message = request.POST.get("message")
        print(f'{name}, {number}, {message}')
    return render(request, 'catalog/contacts.html')

 def product(request):

    product_list = Product.objects.all()

    context = {
        'title': 'Карточка товара',
        'object_list': product_list
     }

    return render(request, 'product_list.html', context)
