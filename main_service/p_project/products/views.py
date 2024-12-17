from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.models import Category, Order, Product, ProductCategory, Review, Seller, SellerUser, ShippingAddress, \
    ShopSeller, Shop
from products.serializers import CategorySerializer, OrderSerializer, ProductSerializer, ProductCategorySerializer, \
    ReviewSerializer, SellerSerializer, SellerUserSerializer, ShippingAddressSerializer, ShopSellerSerializer


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProductCategoryListCreateView(ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class SellerListCreateView(ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerUserListCreateView(ListCreateAPIView):
    queryset = SellerUser.objects.all()
    serializer_class = SellerUserSerializer


class SellerUserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = SellerUser.objects.all()
    serializer_class = SellerUserSerializer


class ShippingAddressListCreateView(ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer


class ShippingAddressDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer


class ShopSellerListCreateView(ListCreateAPIView):
    queryset = ShopSeller.objects.all()
    serializer_class = ShopSellerSerializer


class ShopSellerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ShopSeller.objects.all()
    serializer_class = ShopSellerSerializer


class ShopListCreateView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSellerSerializer


class ShopDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSellerSerializer
