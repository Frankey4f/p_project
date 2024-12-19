from products.domain import CategoryDomain, OrderDomain, ProductDomain, ReviewDomain, SellerDomain, \
    ShippingAddressDomain, ShopDomain
from products.repositories import CategoryRepository, OrderRepository, ProductRepository, ReviewRepository, \
    SellerRepository, ShippingAddressesRepository, ShopRepository
from .models import Cart, Product, CartProduct


class CategoryService:
    @staticmethod
    def get_all_categories():
        return CategoryRepository.get_all()

    @staticmethod
    def get_category_by_id(category_id):
        return CategoryRepository.get_by_id(category_id)

    @staticmethod
    def create_category(category_name):
        category = CategoryDomain(
            name=category_name['name'],
            description=category_name['description'],
        )
        return CategoryRepository.create(category)

    @staticmethod
    def update_category(category_id, category_name):
        category = CategoryDomain(
            name=category_name['name'],
            description=category_name['description'],
        )
        return CategoryRepository.update(category, category_id)

    @staticmethod
    def delete_category(category_id):
        return CategoryRepository.delete(category_id)


class OrderService:
    @staticmethod
    def get_all_orders():
        return OrderRepository.get_all()

    @staticmethod
    def get_order_by_id(order_id):
        return OrderRepository.get_by_id(order_id)

    @staticmethod
    def create_order(data):
        order = OrderDomain(
            customer_name=data['customer_name'],
            item=data['item'],
            quantity=data['quantity'],
        )
        return OrderRepository.create(order)

    @staticmethod
    def update_order(order_id, data):
        order = OrderDomain(
            customer_name=data['customer_name'],
            item=data['item'],
            quantity=data['quantity'],
        )
        return OrderRepository.update(order, order_id)

    @staticmethod
    def delete_order(order_id):
        return OrderRepository.delete(order_id)


class ProductService:
    @staticmethod
    def get_all_products():
        return ProductRepository.get_all()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def create_product(data):
        product = ProductDomain(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock=data['stock'],
        )
        return ProductRepository.create(product)

    @staticmethod
    def update_product(product_id, data):
        product = ProductDomain(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock=data['stock'],
        )
        return ProductRepository.update(product, product_id)

    @staticmethod
    def delete_product(product_id):
        return ProductRepository.delete(product_id)


class ReviewService:
    @staticmethod
    def get_all_reviews():
        return ReviewRepository.get_all()

    @staticmethod
    def get_review_by_id(review_id):
        return ReviewRepository.get_by_id(review_id)

    @staticmethod
    def create_review(data):
        review = ReviewDomain(
            rating=data['rating'],
            comment=data['comment'],
        )
        return ReviewRepository.create(review)

    @staticmethod
    def update_review(review_id, data):
        review = ReviewDomain(
            rating=data['rating'],
            comment=data['comment'],
        )
        return ReviewRepository.update(review, review_id)

    @staticmethod
    def delete_review(review_id):
        return ReviewRepository.delete(review_id)


class SellerService:
    @staticmethod
    def get_all_sellers():
        return SellerRepository.get_all()

    @staticmethod
    def get_seller_by_id(seller_id):
        return SellerRepository.get_by_id(seller_id)

    @staticmethod
    def create_seller(data):
        seller = SellerDomain(
            name=data['name'],
            description=data['description'],
        )
        return SellerRepository.create(seller)

    @staticmethod
    def update_seller(seller_id, data):
        seller = SellerDomain(
            name=data['name'],
            description=data['description'],
        )
        return SellerRepository.update(seller, seller_id)

    @staticmethod
    def delete_seller(seller_id):
        return SellerRepository.delete(seller_id)


class ShippingAddressService:
    @staticmethod
    def get_all_shipping_addresses():
        return ShippingAddressesRepository.get_all()

    @staticmethod
    def get_shipping_address_by_id(shipping_address_id):
        return ShippingAddressesRepository.get_by_id(shipping_address_id)

    @staticmethod
    def create_shipping_address(data):
        shipping_address = ShippingAddressDomain(
            address_line=data['address_line'],
            country=data['country'],
            city=data['city'],
            postal_code=data['postal_code'],
        )
        return ShippingAddressesRepository.create(shipping_address)

    @staticmethod
    def update_shipping_address(shipping_address_id, data):
        shipping_address = ShippingAddressDomain(
            address_line=data['address_line'],
            country=data['country'],
            city=data['city'],
            postal_code=data['postal_code'],
        )
        return ShippingAddressesRepository.update(shipping_address, shipping_address_id)

    @staticmethod
    def delete_shipping_address(shipping_address_id):
        return ShippingAddressesRepository.delete(shipping_address_id)


class ShopService:
    @staticmethod
    def get_all_shops():
        return ShopRepository.get_all()

    @staticmethod
    def get_shop_by_id(shop_id):
        return ShopRepository.get_by_id(shop_id)

    @staticmethod
    def create_shop(data):
        shop = ShopDomain(
            name=data['name'],
            description=data['description'],
            address=data['address'],
        )
        return ShopRepository.create(shop)

    @staticmethod
    def update_shop(shop_id, data):
        shop = ShopDomain(
            name=data['name'],
            description=data['description'],
            address=data['address'],
        )
        return ShopRepository.update(shop, shop_id)

    @staticmethod
    def delete_shop(shop_id):
        return ShopRepository.delete(shop_id)


class CartService:
    @staticmethod
    def get_or_create_cart(customer_id):
        cart = Cart.objects.get_or_create(customer_id=customer_id)
        return cart

    @staticmethod
    def add_product_to_cart(cart_id, product_id, quantity=1):
        cart = CartService.get_or_create_cart(cart_id)
        product = Product.objects.get(id=product_id)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        cart_product.quantity += quantity
        cart_product.save()

    @staticmethod
    def get_cart_content(cart_id):
        cart = CartService.get_or_create_cart(cart_id)
        return cart.products.all()

    @staticmethod
    def remove_product_from_cart(cart_id, product_id):
        cart = CartService.get_or_create_cart(cart_id)
        cart_product = CartProduct.objects.filter(cart=cart, product_id=product_id).first()
        if cart_product:
            cart_product.delete()
            return f"Product {product_id} removed from cart."
        else:
            return f"Product {product_id} not found in cart."
