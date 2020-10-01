from django.shortcuts import render, redirect
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')
    query_set = Phone.objects.all()

    if sort == 'price_low':
        query_set = Phone.objects.order_by('price')
    elif sort == 'price_high':
        query_set = Phone.objects.order_by('price').reverse()
    elif sort == 'name':
        query_set = Phone.objects.order_by('name')
    elif not sort:
        query_set = Phone.objects.all()

    context = {
        'phones': query_set
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # phones = Phone.objects.all()

    if slug:
        phone = Phone.objects.get(slug__iexact=slug)
    else:
        return redirect('catalog')

    context = {
        'phone': phone
    }
    return render(request, template, context)


def home_view(request):
    return redirect('catalog')
