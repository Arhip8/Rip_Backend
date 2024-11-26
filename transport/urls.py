from django.urls import path
from . import views

app_name = 'transport'
urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('cont/<int:id>', views.cont, name='cont'),
    path('order/<int:id>', views.order, name='order'),
    path('to_cart/<int:id>', views.add_product_to_cart, name='to_cart'),
]