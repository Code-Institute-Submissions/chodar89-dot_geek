from products.models import ProductBrand, ProductType

def test_context(request):

    nav_menu_brands = ProductBrand.objects.all().filter(is_in_navbar_menu=True)

    nav_menu_category = ProductType.objects.all().filter(is_in_navbar_menu=True)

    context = {
        "nav_menu_brands": nav_menu_brands,
        "nav_menu_category": nav_menu_category,
    }

    return (context)
