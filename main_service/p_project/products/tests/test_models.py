from django.test import TestCase
from django.contrib.auth.models import User

from products.models import Category, Order, Product, Review, Seller, ShippingAddress, Shop, Cart


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test Description",
        )

    def test_category_creation(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "Test Description")

    def test_category_str(self):
        self.assertEqual(str(self.category), "category")


class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testuser123",
        )
        self.order = Order.objects.create(
            customer_name="John Doe",
            item="Test Item",
            quantity=1,
            total_price=100,
            status="Pending",
            user_id=self.user
        )

    def test_order_creation(self):
        self.assertIsInstance(self.order, Order)
        self.assertEqual(self.order.customer_name, "John Doe")
        self.assertEqual(self.order.item, "Test Item")
        self.assertEqual(self.order.quantity, 1)
        self.assertEqual(self.order.total_price, 100)
        self.assertEqual(self.order.status, "Pending")
        self.assertEqual(self.order.user_id, self.user)

    def test_order_str(self):
        self.assertEqual(str(self.order), "order")

    def test_order_quantity_validation(self):
        with self.assertRaises(ValueError):
            Order.objects.create(
                customer_name='Invalid order quantity',
                description='Invalid order quantity description',
                quantity=-1,
                total_price=100,
                status='Pending',
                user_id=self.user,
            )

    def test_order_price_validation(self):
        with self.assertRaises(ValueError):
            Order.objects.create(
                customer_name='Invalid order price',
                description='Invalid order price description',
                quantity=1,
                total_price=-100,
                status='Pending',
                user_id=self.user,
            )

    def test_order_status_validation(self):
        with self.assertRaises(TypeError):
            Order.objects.create(
                customer_name='Invalid order status',
                description='Order status must be a string!',
                quantity=1,
                total_price=100,
                status=1,
                user_id=self.user,
            )


class ProductModelTest(TestCase):
    def setUp(self):
        self.seller = User.objects.create_user(username='seller1', password='password1')

        self.product = Product.objects.create(
            name='Laptop',
            description='A powerful laptop',
            price=1500.00,
            stock=10,
            seller_id=self.seller
        )

    def test_product_creation(self):
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.name, 'Laptop')
        self.assertEqual(self.product.description, 'A powerful laptop')
        self.assertEqual(self.product.price, 1500.00)
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.seller_id, self.seller)

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Laptop')

    def test_product_price_validation(self):
        with self.assertRaises(ValueError):
            Product.objects.create(
                name='Invalid Product',
                description='This product has a negative price',
                price=-100.00,
                stock=5,
                seller_id=self.seller
            )

    def test_product_stock_validation(self):
        with self.assertRaises(ValueError):
            Product.objects.create(
                name='Invalid Product',
                description='This product has a negative stock',
                price=100.00,
                stock=-5,
                seller_id=self.seller
            )


class ReviewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='password1')

        self.product = Product.objects.create(
            name='Laptop',
            description='A powerful laptop',
            price=1500.00,
            stock=10,
            seller_id=self.user)

        self.review = Review.objects.create(
            user_id=self.user,
            product_id=self.product,
            rating=5,
            comment='This laptop is great!')

    def test_review_creation(self):
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.user_id, self.user)
        self.assertEqual(self.review.product_id, self.product)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, 'This laptop is great!')

    def test_refiew_str(self):
        self.assertEqual(str(self.review), 'Review')

    def test_rating_validation(self):
        with self.assertRaises(ValueError):
            Review.objects.create(
                user_id=self.user,
                product_id=self.product,
                rating=-1,
                comment='This laptop is great!'
            )

    def test_comment_validation(self):
        with self.assertRaises(TypeError):
            Review.objects.create(
                user_id=self.user,
                product_id=self.product,
                rating=5,
                comment=123
            )


class SellerTestCase(TestCase):
    def setUp(self):
        self.seller = User.objects.create_user(username='seller1', password='password1')

        self.name = 'test_seller_name'
        self.description = 'This is a test seller.'

    def test_seller_creation(self):
        self.assertIsInstance(self.seller, Seller)

        self.assertEqual(self.seller.name, self.name)
        self.assertEqual(self.seller.description, self.description)

    def test_seller_str(self):
        self.assertEqual(str(self.seller), 'sellers')


class ShippingAddressTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='password1')

        self.address = ShippingAddress.objects.create(
            address_line='123 Main St',
            country='USA',
            city='New York',
            postal_code=10001,
            user_id=self.user
        )

    def test_shipping_address_creation(self):
        self.assertIsInstance(self.address, ShippingAddress)

        self.assertEqual(self.address.address_line, '123 Main St')
        self.assertEqual(self.address.country, 'USA')
        self.assertEqual(self.address.city, 'New York')
        self.assertEqual(self.address.postal_code, 10001)
        self.assertEqual(self.address.user_id, self.user)

    def test_shipping_address_str(self):
        self.assertEqual(str(self.address), 'Shipping address')

    def test_shipping_address_country_validation(self):
        with self.assertRaises(TypeError):
            ShippingAddress.objects.create(
                address_line='123 Main St',
                country=123,
                city='New York',
                postal_code=10001,
                user_id=self.user
            )

    def test_shipping_address_city_validation(self):
        with self.assertRaises(TypeError):
            ShippingAddress.objects.create(
                address_line='123 Main St',
                country='USA',
                city=123,
                postal_code=10001,
                user_id=self.user
            )

    def test_shipping_address_postal_code_validation(self):
        with self.assertRaises(ValueError):
            ShippingAddress.objects.create(
                address_line='123 Main St',
                country='USA',
                city='New York',
                postal_code='10001',
                user_id=self.user
            )


class ShopTestCase(TestCase):
    def setUp(self):
        self.shop = Shop.objects.create(
            name='Test Shop',
            description='Test description',
            address='123 Main St'
        )

    def test_shop_creation(self):
        self.assertIsInstance(self.shop, Shop)

        self.assertEqual(self.shop.name, 'Test Shop')
        self.assertEqual(self.shop.description, 'Test description')
        self.assertEqual(self.shop.address, '123 Main St')

    def test_shop_str(self):
        self.assertEqual(str(self.shop), 'shops')

    def test_shop_name_validation(self):
        with self.assertRaises(TypeError):
            Shop.objects.create(
                name=123,
                description='Test description',
                address='123 Main St'
            )

    def test_shop_description_validation(self):
        with self.assertRaises(TypeError):
            Shop.objects.create(
                name='Test Shop',
                description=123,
                address='123 Main St'
            )

    def test_shop_address_validation(self):
        with self.assertRaises(TypeError):
            Shop.objects.create(
                name='Test Shop',
                description='Test description',
                address=123
            )


class CartTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='password1')

        self.cart = Cart.objects.create(
            user=self.user,
            products=Product.objects.create(
                name='Product 1',
                price=100,
                stock=10),
        )

    def test_cart_creation(self):
        self.assertIsInstance(self.cart, Cart)
        self.assertEqual(self.cart.user, self.user)
        self.assertEqual(self.cart.products.name, 'Product 1')
        self.assertEqual(self.cart.products.price, 100)
        self.assertEqual(self.cart.products.stock, 10)

    def test_cart_str(self):
        self.assertEqual(str(self.cart), f'Cart of {self.user.username}')

    def test_user_validation(self):
        with self.assertRaises(TypeError):
            Cart.objects.create(
                user=123,
                products=Product.objects.create(
                    name='Product 1',
                    price=100,
                    stock=10)
            )

    def test_product_validation(self):
        with self.assertRaises(TypeError):
            Cart.objects.create(
                user=self.user,
                products=123
            )
