from django.test import TestCase
from datetime import datetime
from products.domain import \
    CategoryDomain, \
    OrderDomain, \
    ProductDomain, \
    ReviewDomain, \
    SellerDomain, \
    ShippingAddressDomain


class DomainModelsTest(TestCase):

    def test_category_domain_creation(self):
        category = CategoryDomain(id=1, name='Books', description='All kinds of books', created_at=datetime.now())

        self.assertEqual(category.id, 1)
        self.assertEqual(category.name, 'Books')
        self.assertEqual(category.description, 'All kinds of books')
        self.assertIsInstance(category.created_at, datetime)

    def test_order_domain_creation(self):
        order = OrderDomain(id=1, customer_name='John Doe', item='Book', quantity=2, total_price=39.98,
                            status='Pending', created_at=datetime.now())

        self.assertEqual(order.id, 1)
        self.assertEqual(order.customer_name, 'John Doe')
        self.assertEqual(order.item, 'Book')
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.total_price, 39.98)
        self.assertEqual(order.status, 'Pending')
        self.assertIsInstance(order.created_at, datetime)

    def test_product_domain_creation(self):
        product = ProductDomain(id=1, name='Book', description='A great book', price=19.99, stock=True,
                                created_at=datetime.now())

        self.assertEqual(product.id, 1)
        self.assertEqual(product.name, 'Book')
        self.assertEqual(product.description, 'A great book')
        self.assertEqual(product.price, 19.99)
        self.assertTrue(product.stock)
        self.assertIsInstance(product.created_at, datetime)

    def test_review_domain_creation(self):
        review = ReviewDomain(id=1, rating=4.5, comment='Great product!', created_at=datetime.now())

        self.assertEqual(review.id, 1)
        self.assertEqual(review.rating, 4.5)
        self.assertEqual(review.comment, 'Great product!')
        self.assertIsInstance(review.created_at, datetime)

    def test_seller_domain_creation(self):
        seller = SellerDomain(id=1, name='Book Seller', description='Sells various books', created_at=datetime.now())

        self.assertEqual(seller.id, 1)
        self.assertEqual(seller.name, 'Book Seller')
        self.assertEqual(seller.description, 'Sells various books')
        self.assertIsInstance(seller.created_at, datetime)

    def test_shipping_address_domain_creation(self):
        shipping_address = ShippingAddressDomain(id=1, address_line='123 Main St', country='USA', city='New York',
                                                 postal_code=10001, created_at=datetime.now())

        self.assertEqual(shipping_address.id, 1)
        self.assertEqual(shipping_address.address_line, '123 Main St')
        self.assertEqual(shipping_address.country, 'USA')
        self.assertEqual(shipping_address.city, 'New York')
        self.assertEqual(shipping_address.postal_code, 10001)
        self.assertIsInstance(shipping_address.created_at, datetime)
