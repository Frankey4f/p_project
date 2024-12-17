from rest_framework import serializers
from products.models import Category, Order, Product, ProductCategory, Review, Seller, SellerUser, ShippingAddress, \
    ShopSeller, Shop


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SellerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerUser
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopSeller
        fields = '__all__'
