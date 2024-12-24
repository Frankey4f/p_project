from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from products.services import CategoryService, OrderService, ProductService, ReviewService, SellerService, \
    ShippingAddressService, ShopService, CartService


class CategoryListView(APIView):
    def get(self, request):
        categories = CategoryService.get_all_categories()
        return Response([product.__dict__ for product in categories], status=status.HTTP_200_OK)

    def post(self, request):
        category = CategoryService.create_category(request.data)
        return Response(category.__dict__, status=status.HTTP_201_CREATED)


class CategoryDetailView(APIView):
    def get(self, request, category_id):
        category = CategoryService.get_category_by_id(category_id)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(category.__dict__, status=status.HTTP_200_OK)

    def put(self, request, category_id):
        category = CategoryService.update_category(category_id, request.data)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(category.__dict__, status=status.HTTP_200_OK)

    def delete(self, request, category_id):
        CategoryService.delete_category(category_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderListView(APIView):
    def get(self, request):
        orders = OrderService.get_all_orders()
        return Response([order.__dict__ for order in orders], status=status.HTTP_200_OK)

    def post(self, request):
        order = OrderService.create_order(request.data)
        return Response(order.__dict__, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    def get(self, request, order_id):
        order = OrderService.get_order_by_id(order_id)
        if not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(order.__dict__, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        order = OrderService.update_order(order_id, request.data)
        if not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(order.__dict__, status=status.HTTP_200_OK)

    def delete(self, request, order_id):
        OrderService.delete_order(order_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListView(APIView):
    def get(self, request):
        products = ProductService.get_all_products()
        return Response([product.__dict__ for product in products], status=status.HTTP_200_OK)

    def post(self, request):
        product = ProductService.create_product(request.data)
        return Response(product.__dict__, status=status.HTTP_201_CREATED)


class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(product.__dict__, status=status.HTTP_200_OK)

    def put(self, request, product_id):
        product = ProductService.update_product(product_id, request.data)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(product.__dict__, status=status.HTTP_200_OK)


class ReviewListView(APIView):
    def get(self, request):
        reviews = ReviewService.get_all_reviews()
        return Response([review.__dict__ for review in reviews], status=status.HTTP_200_OK)

    def post(self, request):
        review = ReviewService.create_review(request.data)
        return Response(review.__dict__, status=status.HTTP_201_CREATED)


class ReviewDetailView(APIView):
    def get(self, request, review_id):
        review = ReviewService.get_review_by_id(review_id)
        if not review:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(review.__dict__, status=status.HTTP_200_OK)

    def put(self, request, review_id):
        review = ReviewService.update_review(review_id, request.data)
        if not review:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(review.__dict__, status=status.HTTP_200_OK)

    def delete(self, request, review_id):
        ReviewService.delete_review(review_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellerListView(APIView):
    def get(self, request):
        sellers = list(product.seller for product in ProductService.get_all_products())
        return Response([seller.__dict__ for seller in sellers], status=status.HTTP_200_OK)

    def post(self, request):
        seller = SellerService.create_seller(request.data)
        return Response(seller.__dict__, status=status.HTTP_201_CREATED)


class SellerDetailView(APIView):
    def get(self, request, seller_id):
        seller = SellerService.get_seller_by_id(seller_id)
        if not seller:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(seller.__dict__, status=status.HTTP_200_OK)

    def put(self, request, seller_id):
        seller = SellerService.update_seller(seller_id, request.data)
        if not seller:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(seller.__dict__, status=status.HTTP_200_OK)

    def delete(self, request, seller_id):
        SellerService.delete_seller(seller_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShippingAddressListView(APIView):
    def get(self, request):
        shipping_addresses = list(order.shipping_address for order in OrderService.get_all_orders())
        return Response([address.__dict__ for address in shipping_addresses], status=status.HTTP_200_OK)

    def post(self, request):
        address = ShippingAddressService.create_shipping_address(request.data)
        return Response(address.__dict__, status=status.HTTP_201_CREATED)


class ShippingAddressDetailView(APIView):
    def get(self, request, address_id):
        address = ShippingAddressService.get_shipping_address_by_id(address_id)
        if not address:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(address.__dict__, status=status.HTTP_200_OK)

    def put(self, request, address_id):
        address = ShippingAddressService.update_shipping_address(address_id, request.data)
        if not address:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(address.__dict__, status=status.HTTP_200_OK)

    def delete(self, request, address_id):
        ShippingAddressService.delete_shipping_address(address_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShopListView(APIView):
    def get(self, request):
        shops = list(seller.shop for seller in SellerService.get_all_sellers())
        return Response([shop.__dict__ for shop in shops], status=status.HTTP_200_OK)

    def post(self, request):
        shop = ShopService.create_shop(request.data)
        return Response(shop.__dict__, status=status.HTTP_201_CREATED)


class ShopDetailView(APIView):
    def get(self, request, shop_id):
        shop = ShopService.get_shop_by_id(shop_id)
        if not shop:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(shop.__dict__, status=status.HTTP_200_OK)

    def put(self, request, shop_id):
        shop = ShopService.update_shop(shop_id, request.data)
        if not shop:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(shop.__dict__, status=status.HTTP_200_OK)

    def delete(self, request, shop_id):
        ShopService.delete_shop(shop_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        quantity = request.data.get('quantity', 1)
        user = request.user
        cart_product = CartService.add_product_to_cart(user=user, product_id=product_id, quantity=quantity)
        return Response(
            {
                'message': f'Product {cart_product.product.name} added to cart',
                'quantity': cart_product.quantity
            },
            status=status.HTTP_200_OK
        )


class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart_content = CartService.get_cart_content(user=user)
        data = [{"name": p.name, "price": p.price, "quantity": c.quantity} for p, c in cart_content]
        return Response({"cart": data}, status=status.HTTP_200_OK)


class CartRemoveView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id, cart_id):
        CartService.remove_product_from_cart(cart_id, product_id)
        return Response("message: Product removed from cart successfully", status=status.HTTP_204_NO_CONTENT)


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0OTQxNTcxLCJpYXQiOjE3MzQ5NDEyNzEsImp0aSI6IjIyNGY0ZWRkYTVhOTQzNDhiN2JkYjhiMWY4M2RkMDE3IiwidXNlcl9pZCI6OH0.l0HL_9heOO4c1jmoyjdElOI7C1xc9gHmsDjCs9CL2pw