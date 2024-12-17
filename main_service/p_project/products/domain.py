from dataclasses import dataclass
from datetime import datetime


@dataclass
class CategoryDomain:
    id: int = None
    name: str = ''
    description: str = ''
    created_at: datetime = None


@dataclass
class OrderDomain:
    id: int = None
    customer_name: str = ''
    item: str = ''
    quantity: int = 0
    total_price: float = 0.0
    status: str = ''
    created_at: datetime = None
    updated_at: datetime = None
    user_id: int = None


@dataclass
class ProductDomain:
    id: int = None
    name: str = ''
    description: str = ''
    price: float = 0.0
    stock: bool = False
    created_at: datetime = None
    updated_at: datetime = None
    user_id: int = None


@dataclass
class ProductCategoryDomain:
    product: int = None
    category: int = None


@dataclass
class ReviewDomain:
    id: int = None
    rating: float = 0.0
    comment: str = ''
    created_at: datetime = None
    updated_at: datetime = None
    product_id: int = None


@dataclass
class SellerDomain:
    id: int = None
    name: str = ''
    description: str = ''
    created_at: datetime = None


@dataclass
class SellerUserDomain:
    seller: int = None
    user: int = None


@dataclass
class ShippingAddressDomain:
    id: int = None
    address_line: str = ''
    country: str = ''
    city: str = ''
    postal_code: int = 0
    created_at: datetime = None
    updated_at: datetime = None
    user_id: int = None


@dataclass
class ShopDomain:
    id: int = None
    name: str = ''
    description: str = ''
    address: str = ''
    created_at: datetime = None
    updated_at: datetime = None


@dataclass
class ShopSellerDomain:
    shop: int = None
    seller: int = None
