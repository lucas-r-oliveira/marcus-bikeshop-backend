from sqlalchemy import (
    TEXT,
    Boolean,
    Column,
    ForeignKey,
    MetaData,
    String,
    Table,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import UUID

from common import MoneyType
from product.domain import model


metadata = MetaData()


part_option = Table(
    "part_options",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("name", String(255)),
    Column("in_stock", Boolean, default=True),
    Column("product_part_id", UUID, ForeignKey("product_parts.id"))
)

# product and product part have a m2m relationship
product_part = Table(
    "product_parts",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("name", String(255)),
    Column("description", String(511)),

    #TODO: review
    # Column("part_option_id", ForeignKey("part_option.id")),
    Column("product_id", UUID, ForeignKey("products.id")),
)

product = Table(
    "products",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("name", String(255)),
    Column("description", String(511)),
    Column("base_price", MoneyType),
    Column("image_url", TEXT),
    Column("category", String(63))
)

def start_mappers(mapper_registry):
    mapper_registry.map_imperatively(
        model.PartOption,
        part_option,
        properties={
            "id": part_option.c.id,
            "name": part_option.c.name,
            "in_stock": part_option.c.in_stock,
        }
    )

    mapper_registry.map_imperatively(
        model.ProductPart,
        product_part,
        properties={
            "id": product_part.c.id,
            "name": product_part.c.name,
            "description": product_part.c.description,
            "options": relationship(model.PartOption, backref="product_part"),
        }
    )

    mapper_registry.map_imperatively(
        model.Product,
        product,
        properties={
            "id": product.c.id,
            "name": product.c.name,
            "description": product.c.description,
            "base_price": product.c.base_price,
            "image_url": product.c.image_url,
            "category": product.c.category,
            "parts": relationship(model.ProductPart, backref="product"),
        }
    )
