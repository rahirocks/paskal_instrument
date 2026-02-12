from decimal import Decimal
from .models import Product

CART_SESSION_KEY = "cart"

def get_cart(request):
    return request.session.get(CART_SESSION_KEY,{})

def save_cart(request, cart):
    request.session[CART_SESSION_KEY] = cart
    request.session.modified = True

def add_to_cart(request, product_id, qty=1):
    cart = get_cart(request)
    pid =str(product_id)
    cart[pid] = cart.get(pid,0)+int(qty)
    save_cart(request,cart)

def remove_from_cart(request, product_id):
    cart = get_cart(request)
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
        save_cart(request,cart)

def update_qty(request, product_id, qty):
    cart= get_cart(request)
    pid = str(product_id)
    qty = int(qty)
    if qty<=0:
        cart.pop(pid,None)
    else:
        cart[pid] = qty
    save_cart(request,cart)

def clear_cart(request):
    save_cart(request,{})

def cart_items_with_totals(request):
    cart= get_cart(request)
    ids = [int(pid) for pid in cart.keys()] if cart else []
    products = Product.objects.filter(id__in =ids, is_active = True) if ids else Product.objects.none()

    product_map = {p.id: p for p in products}
    items =[]
    subtotal = Decimal("0.00")

    for pid_str, qty in cart.items():
        pid = int(pid_str)
        p = product_map.get(pid)
        if not p: 
            continue
        qty = int(qty)
        line_total = p.price * qty
        subtotal += line_total
        items.append({
            "product":p,
            "qty": qty,
            "line_total":line_total,
        })
    return items, subtotal

