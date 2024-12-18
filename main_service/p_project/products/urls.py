from django.urls import path
from .views import AddToCartView, CartDetailView

from products.views import CategoryListView, CategoryDetailView, OrderListView, OrderDetailView, ProductListView, \
    ProductDetailView, ReviewListView, ReviewDetailView, SellerListView, SellerDetailView, ShippingAddressListView, \
    ShippingAddressDetailView, ShopListView, ShopDetailView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('order/', OrderListView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('product/', ProductListView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('review/', ReviewListView.as_view(), name='review-list-create'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('seller/', SellerListView.as_view(), name='seller-list-create'),
    path('seller/<int:pk>/', SellerDetailView.as_view(), name='seller-detail'),
    path('shipping_address/', ShippingAddressListView.as_view(), name='shipping-address-list-create'),
    path('shipping_address/<int:pk>/', ShippingAddressDetailView.as_view(), name='shipping-address-detail'),
    path('shop/', ShopListView.as_view(), name='shop-list-create'),
    path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('api/cart/add/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('api/cart/', CartDetailView.as_view(), name='cart-detail'),
]
