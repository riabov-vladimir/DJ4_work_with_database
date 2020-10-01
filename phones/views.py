from django.shortcuts import render, redirect
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'

    query_set = Phone.objects.all()

    context = {
        'phones': query_set
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    
    context = {}
    return render(request, template, context)

def home_view(request):
    return redirect('catalog')
