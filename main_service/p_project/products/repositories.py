from .models import Category, Order, Product, Review, Seller, Shop, ShippingAddress

from products.domain import CategoryDomain, OrderDomain, ProductDomain, ReviewDomain, SellerDomain, ShopDomain


class CategoryRepository:
    @staticmethod
    def get_all():
        return [CategoryDomain(
            id=Category.id,
            name=Category.name,
            description=Category.description,
            created_at=Category.created_at,
        ) for category in Category.objects.all()]

    @staticmethod
    def get_by_id(category_id):
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return None
        return CategoryDomain(
            id=category.id,
            name=category.name,
            description=category.description,
            created_at=category.created_at,
        )

    @staticmethod
    def create(domain_model):
        category = Category.objects.create(
            name=domain_model.name,
            description=domain_model.description,
        )
        return CategoryDomain(
            id=category.id,
            name=category.name,
            description=category.description,
            created_at=category.created_at,
        )

    @staticmethod
    def update(category_id, domain_model):
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return None
        category.name = domain_model.name
        category.description = domain_model.description
        category.save()
        return CategoryDomain(
            id=category.id,
            name=category.name,
            description=category.description,
            created_at=category.created_at,
        )

    @staticmethod
    def delete(category_id):
        Category.objects.filter(id=category_id).delete()


class OrderRepository:
    @staticmethod
    def get_all():
        return [OrderDomain(
            id=Order.id,
            customer_name=Order.customer_name,
            item=Order.item,
            quantity=Order.quantity,
            total_price=Order.total_price,
            status=Order.status,
            created_at=Order.created_at,
            updated_at=Order.updated_at,
        ) for order in Order.objects.all()]

    @staticmethod
    def get_by_id(order_id):
        order = Order.objects.filter(id=order_id).first()
        if not order:
            return None
        return OrderDomain(
            id=order.id,
            customer_name=order.customer_name,
            item=order.item,
            quantity=order.quantity,
            total_price=order.total_price,
            status=order.status,
            created_at=order.created_at,
            updated_at=order.updated_at,
        )

    @staticmethod
    def create(domain_model):
        order = Order.objects.create(
            customer_name=domain_model.customer_name,
            item=domain_model.item,
            quantity=domain_model.quantity,
        )
        return OrderDomain(
            id=order.id,
            customer_name=order.customer_name,
            item=order.item,
            quantity=order.quantity,
        )

    @staticmethod
    def update(order_id, domain_model):
        order = Order.objects.filter(id=order_id).first()
        if not order:
            return None
        order.customer_name = domain_model.customer_name
        order.item = domain_model.item
        order.quantity = domain_model.quantity
        order.save()
        return OrderDomain(
            id=order.id,
            customer_name=order.customer_name,
            item=order.item,
            quantity=order.quantity,
            total_price=order.total_price,
            status=order.status,
            updated_at=order.updated_at,
        )

    @staticmethod
    def delete(order_id):
        Order.objects.filter(id=order_id).delete()


class ProductRepository:
    @staticmethod
    def get_all():
        return [ProductDomain(
            id=Product.id,
            name=Product.name,
            description=Product.description,
            price=Product.price,
            stock=Product.stock,
            created_at=Product.created_at,
            updated_at=Product.updated_at,
        ) for product in Product.objects.all()]

    @staticmethod
    def get_by_id(product_id):
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return None
        return ProductDomain(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )

    @staticmethod
    def create(domain_model):
        product = Product.objects.create(
            name=domain_model.name,
            description=domain_model.description,
            price=domain_model.price,
        )
        return ProductDomain(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )

    @staticmethod
    def update(product_id, domain_model):
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return None
        product.name = domain_model.name
        product.description = domain_model.description
        product.price = domain_model.price
        product.stock = domain_model.stock
        product.save()
        return ProductDomain(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )

    @staticmethod
    def delete(product_id):
        Product.objects.filter(id=product_id).delete()


class ReviewRepository:
    @staticmethod
    def get_all():
        return [ReviewDomain(
            id=Review.id,
            rating=Review.rating,
            comment=Review.comment,
            created_at=Review.created_at,
            updated_at=Review.updated_at,
            user_id=Review.user_id,
        ) for review in Review.objects.all()]

    @staticmethod
    def get_by_id(review_id):
        review = Review.objects.filter(id=review_id).first()
        if not review:
            return None
        return ReviewDomain(
            id=review.id,
            rating=review.rating,
            comment=review.comment,
            created_at=review.created_at,
            updated_at=review.updated_at,
            user_id=review.user_id,
        )

    @staticmethod
    def create(domain_model):
        review = Review.objects.create(
            rating=domain_model.rating,
            comment=domain_model.comment,
        )
        return ReviewDomain(
            id=review.id,
            rating=review.rating,
            comment=review.comment,
            created_at=review.created_at,
            user_id=review.user_id
        )

    @staticmethod
    def update(review_id, domain_model):
        review = Review.objects.filter(id=review_id).first()
        if not review:
            return None
        review.rating = domain_model.rating
        review.comment = domain_model.comment
        return ReviewDomain(
            id=review.id,
            rating=review.rating,
            comment=review.comment,
            created_at=review.created_at,
            updated_at=review.updated_at,
            user_id=review.user_id
        )

    @staticmethod
    def delete(review_id):
        Review.objects.filter(id=review_id).delete()


class SellerRepository:
    @staticmethod
    def get_all():
        return [SellerDomain(
            id=Seller.id,
            name=Seller.name,
            description=Seller.description,
            created_at=Seller.created_at,
            updatet_at=Seller.updated_at,
        ) for review in Seller.objects.all()]

    @staticmethod
    def get_by_id(seller_id):
        seller = Seller.objects.filter(id=seller_id).first()
        if not seller:
            return None
        return SellerDomain(
            id=seller.id,
            name=seller.name,
            description=seller.description,
            created_at=seller.created_at,
            updated_at=seller.updated_at,
        )

    @staticmethod
    def create(domain_model):
        seller = Seller.objects.create(
            name=domain_model.name,
            description=domain_model.description,
        )
        return SellerDomain(
            id=seller.id,
            name=seller.name,
            description=seller.description,
            created_at=seller.created_at,
            updated_at=seller.updated_at,
        )

    @staticmethod
    def update(seller_id, domain_model):
        seller = Seller.objects.filter(id=seller_id).first()
        if not seller:
            return None
        return SellerDomain(
            name=seller.name,
            description=seller.description,
        )

    @staticmethod
    def delete(seller_id):
        Seller.objects.filter(id=seller_id).delete()


class ShippingAddressesRepository:
    @staticmethod
    def get_all():
        return [ShopDomain(
            id=ShippingAddress.id,
            address=ShippingAddress.address_line,
            country=ShippingAddress.country,
            city=ShippingAddress.city,
            postal_code=ShippingAddress.postal_code,
            created_at=ShippingAddress.created_at,
            user_id=ShippingAddress.user_id,
        ) for address in ShippingAddress.objects.all()]

    @staticmethod
    def get_by_id(shippingaddress_id):
        shippingaddress = ShippingAddress.objects.filter(id=shippingaddress_id).first()
        if not shippingaddress:
            return None
        return ShippingAddress(
            id=shippingaddress.id,
            address=shippingaddress.address_line,
            country=shippingaddress.country,
            city=shippingaddress.city,
            postal_code=shippingaddress.postal_code,
            created_at=shippingaddress.created_at,
            user_id=shippingaddress.user_id
        )

    @staticmethod
    def create(domain_model):
        shippingaddress = ShippingAddress.objects.create(
            address=ShippingAddress.address_line,
            country=ShippingAddress.country,
            city=ShippingAddress.city,
            postal_code=ShippingAddress.postal_code,
        )
        return ShippingAddress(
            id=shippingaddress.id,
            address=shippingaddress.address_line,
            country=shippingaddress.country,
            city=shippingaddress.city,
            postal_code=shippingaddress.postal_code,
            created_at=shippingaddress.created_at,
            user_id=shippingaddress.user_id,
        )

    @staticmethod
    def update(shippingaddress_id, domain_model):
        shippingaddress = ShippingAddress.objects.filter(id=shippingaddress_id).first()
        if not shippingaddress:
            return None
        shippingaddress.address = ShippingAddress.address_line
        shippingaddress.country = ShippingAddress.country
        shippingaddress.city = ShippingAddress.city
        shippingaddress.postal_code = ShippingAddress.postal_code
        return ShippingAddress(
            id=shippingaddress.id,
            address=shippingaddress.address_line,
            country=shippingaddress.country,
            city=shippingaddress.city,
            postal_code=shippingaddress.postal_code,
        )

    @staticmethod
    def delete(shippingaddress_id):
        ShippingAddress.objects.filter(id=shippingaddress_id).delete()


class ShopRepository:
    @staticmethod
    def get_all():
        return [ShopDomain(
            id=Shop.id,
            name=Shop.name,
            description=Shop.description,
            address=Shop.address,
            created_at=Shop.created_at,
            updated_at=Shop.updated_at,
        ) for address in Shop.objects.all()]

    @staticmethod
    def get_by_id(shop_id):
        shop = Shop.objects.filter(id=shop_id).first()
        if not shop:
            return None
        return Shop(
            id=shop.id,
            name=shop.name,
            description=shop.description,
            address=shop.address,
            created_at=shop.created_at,
            updated_at=shop.updated_at,
        )

    @staticmethod
    def create(shop_model):
        shop = Shop.objects.create(
            name=shop_model.name,
            description=shop_model.description,
            address=shop_model.address,
        )
        return Shop(
            id=shop.id,
            name=shop.name,
            description=shop.description,
            address=shop.address,
            created_at=shop.created_at,
        )

    @staticmethod
    def update(shop_id, shop_model):
        shop = Shop.objects.filter(id=shop_id).first()
        if not shop:
            return None
        shop.name = shop_model.name
        shop.description = shop_model.description
        shop.address = shop_model.address
        return Shop(
            id=shop.id,
            name=shop.name,
            description=shop.description,
            address=shop.address,
            created_at=shop.created_at,
            updated_at=shop.updated_at,
        )

    @staticmethod
    def delete(shop_id):
        Shop.objects.filter(id=shop_id).delete()
