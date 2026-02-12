from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Product, Order,OrderItem
from .forms import CheckoutForm
from .cart import add_to_cart, remove_from_cart, update_qty, clear_cart, cart_items_with_totals

def home(request):
    featured = Product.objects.filter(is_active=True)[:6]
    return render(request, "core/home.html",{"featured":featured})


def products(request):
    items = Product.objects.filter(is_active = True).order_by("id")
    return render(request,"core/products.html",{"items":items})

def about(request):
    return render(request,"core/about.html")

def cart_view(request):
    items, subtotal = cart_items_with_totals(request)
    return render(request,"core/cart.html",{"items":items,"subtotal":subtotal})

@require_POST
def cart_add(request, product_id):
    qty = request.POST.get("qty",1)
    add_to_cart(request,product_id,qty)
    return redirect("cart")

@require_POST
def cart_remove(request, product_id):
    remove_from_cart(request,product_id)
    return redirect("cart")

@require_POST
def cart_update(request, product_id):
    qty = request.POST.get("qty",1)
    update_qty(request,product_id,qty)
    return redirect("cart")

def checkout(request):
    items, subtotal = cart_items_with_totals(request)
    if not items:
        return redirect("products")
    
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(**form.cleaned_data)

            for line in items:
                p = line["product"]
                qty = line["qty"]
                OrderItem.objects.create(
                    order = order,
                    product=p,
                    quantity = qty,
                    unit_price = p.price
                )
            clear_cart(request)
            return render(request, "core/checkout_success.html",{"order":order})
        
    else:
        form =CheckoutForm()

    return render(request, "core/checkout.html",{
        "form":form,
        "items":items,
        "subtotal":subtotal
    })