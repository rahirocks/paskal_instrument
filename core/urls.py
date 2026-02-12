from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path("products/",views.products, name = "products"),
    path("about/", views.about, name = "about"),

    path("cart/", views.cart_view,name="cart"),
    path("cart/add/<int:product_id>/",views.cart_add, name="cart_add"),
    path("cart/remove/<int:product_id>/",views.cart_remove,name="cart_remove"),
    path("cart/update/<int:product_id>/",views.cart_update,name="cart_update"),

    path("checkout/", views.checkout,name="checkout"),

]

