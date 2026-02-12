from enum import Enum


class Topic(str, Enum):
    USER = "user"
    ORDER = "order"
    POST = "post"
    PRODUCT = "product"
    SUPPLIER = "supplier"

    @classmethod
    def all(cls) -> list[str]:
        return [topic.value for topic in cls]


class EventType(str, Enum):
    """Event types (topic.action)."""
    
    USER_CREATED = "user.created"
    USER_UPDATED = "user.updated"
    USER_DELETED = "user.deleted"

    SUPPLIER_CREATED = "supplier.created"
    SUPPLIER_UPDATED = "supplier.updated"
    SUPPLIER_DELETED = "supplier.deleted"

    PRODUCT_CREATED = "product.created"
    PRODUCT_UPDATED = "product.updated"
    PRODUCT_PUBLISHED = "product.published"
    PRODUCT_DISCONTINUED = "product.discontinued"
    PRODUCT_OUT_OF_STOCK = "product.out_of_stock"
    PRODUCT_RESTORED = "product.restored"
    PRODUCT_DELETED = "product.deleted"

    POST_CREATED = "post.created"
    POST_UPDATED = "post.updated"
    POST_PUBLISHED = "post.published"
    POST_DELETED = "post.deleted"

    ORDER_CREATED = "order.created"
    ORDER_CANCELLED = "order.cancelled"
