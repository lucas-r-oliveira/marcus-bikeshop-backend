from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Table,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import UUID

from common import MoneyType
from orders.domain import model

from common import metadata


cart_item = Table(
    "cart_items",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("product_id", UUID, ForeignKey("products.id")),
    Column("cart_id", UUID, ForeignKey("carts.id")),
    Column("part_option_id", Integer, ForeignKey("part_options.id")) ,
    Column("unit_price", MoneyType),
    Column("qty", Integer, default=1)

)

cart = Table(
    "carts",
    metadata,
    Column("id", UUID, primary_key=True),
    # Column("user_id", UUID, ForeignKey("user.id")),
)

def start_mappers(mapper_registry):
    mapper_registry.map_imperatively(
        model.CartItem,
        cart_item,
        properties={
            "id": cart_item.c.id,
            "product_id": cart_item.c.product_id,
            #TODO: "part_config_id": cart_item.c.product_id,
            "unit_price": cart_item.c.unit_price,
            "qty": cart_item.c.qty,
        }
    )

    mapper_registry.map_imperatively(
        model.Cart,
        cart,
        properties={
            "id": cart.c.id,
            #TODO: "user_id": cart.c.user_id,
            "cart_items": relationship(model.CartItem, backref="cart"),
        }
    )
