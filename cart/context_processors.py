from django.core.exceptions import ObjectDoesNotExist

from cart.models import Cart, CartItem
from cart.views import _cart_id, _get_user_or_none


def cart_details(request, total=0, counter=0, cart_items=None):
    """
    Check all items in cart, count qnty and total price and
    return dict as a context processors so it can be displayed in nav bar
    """
    user_id = _get_user_or_none(request)
    session_cart_id = _cart_id(request)
    try:
        if user_id:
            cart = Cart.objects.get(user=user_id)
        else:
            cart = Cart.objects.get(cart_id=session_cart_id)
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            counter += item.quantity
    except ObjectDoesNotExist:
        pass
    return dict(cart_items=cart_items, total=total,counter=counter)
