from django.urls import path

from .views import CategoryListCreateView, CategoryDetailView, OrderListCreateView, OrderDetailView, \
    ProductListCreateView, ProductDetailView, ReviewListCreateView, ReviewDetailView, ProductCategoryListCreateView, \
    ProductCategoryDetailView, SellerListCreateView, SellerDetailView, SellerUserListCreateView, SellerUserDetailView, \
    ShippingAddressListCreateView, ShippingAddressDetailView, ShopListCreateView, ShopDetailView, \
    ShopSellerListCreateView, ShopSellerDetailView

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('order/', OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('review/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('product_category/', ProductCategoryListCreateView.as_view(), name='product-category-list-create'),
    path('product_category/<int:pk>/', ProductCategoryDetailView.as_view(), name='product-category-detail'),
    path('seller/', SellerListCreateView.as_view(), name='seller-list-create'),
    path('seller/<int:pk>/', SellerDetailView.as_view(), name='seller-detail'),
    path('seller_user/', SellerUserListCreateView.as_view(), name='seller-user-list-create'),
    path('seller_user/<int:pk>/', SellerUserDetailView.as_view(), name='seller-user-detail'),
    path('shipping_address/', ShippingAddressListCreateView.as_view(), name='shipping-address-list-create'),
    path('shipping_address/<int:pk>/', ShippingAddressDetailView.as_view(), name='shipping-address-detail'),
    path('shop/', ShopListCreateView.as_view(), name='shop-list-create'),
    path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('shop_seller/', ShopSellerListCreateView.as_view(), name='shop-seller-list-create'),
    path('shop_seller/<int:pk>/', ShopSellerDetailView.as_view(), name='shop-seller-detail'),
]
