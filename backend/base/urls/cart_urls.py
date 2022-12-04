from django.urls import path
from base.views import cart_views as views


urlpatterns = [
     path('mycarts/', views.getCarts, name='mycarts'),
     path('add/', views.addCartItems, name='carts-add'),
     path('delete/<str:pk>/', views.deleteCartItems, name='cartitems-delete'),
     path('delete/<str:pk>/', views.deleteCart, name='cart-delete'),
     path('update/<str:pk>/', views.updateCart, name="cart-update"),
]
