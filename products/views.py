from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, SizeChart, ProductBrand


def all_products(request):
    """ Get all products and size chart than pass it and render """

    # Get all products ordered by - newest first
    get_all_products = Product.objects.filter(
        is_for_sale=True).order_by('-created_at')

    size_chart = SizeChart.objects.all()

    paginator = Paginator(get_all_products, 9)

    page = request.GET.get('page')

    paged_products = paginator.get_page(page)

    context = {
        'all_products': paged_products,
        'size_chart': size_chart,
    }
    return render(request, 'products/all_products.html', context)


def product(request, product_id):
    """ Single product page, get product id and render html with product details """

    get_product = get_object_or_404(Product, pk=product_id)

    size_chart = SizeChart.objects.all()

    context = {
        'product': get_product,
        'size_chart': size_chart,
    }

    return render(request, 'products/product.html', context)
