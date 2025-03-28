from sqlalchemy import (
    TEXT,
    Boolean,
    Column,
    ForeignKey,
    String,
    Table,
    Integer
)

from sqlalchemy.orm import backref, properties, relationship
from sqlalchemy.schema import ColumnCollectionMixin
from sqlalchemy.sql.sqltypes import UUID

from common import MoneyType, metadata
from product.domain import model


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

#part_configuration = Table(
#    "part_configurations",
#    metadata,
#    Column("id", UUID, primary_key=True),
#    Column("product_id", UUID, ForeignKey("products.id")),
#    Column("part_id", UUID, ForeignKey("product_parts.id"))
#)
#
#part_configuration_options = Table(
#    "part_configuration_options",
#    metadata,
#    Column("id", UUID, primary_key=True),
#    Column("configuration_id", UUID, ForeignKey("part_configurations.id")),
#    Column("option_id", UUID, ForeignKey("part_options.id")),
#)
part_configuration = Table(
    "part_configurations",
    metadata,
    Column("product_id", UUID, ForeignKey("products.id"), primary_key=True),
    Column("part_id", UUID, ForeignKey("product_parts.id"), primary_key=True),
    Column("option_id", UUID, ForeignKey("part_options.id"), primary_key=True),
)
# do I need a m2m table here?

characteristic_option = Table(
    "characteristic_options",
    metadata, 
    # TODO m2m product
    Column("id", String(255), primary_key=True),
    Column("name", String(255)),
    Column("type", String(63)),
    Column("in_stock", Boolean)
)

product_characteristic_options = Table(
    "product_characteristic_options",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("product_id", UUID, ForeignKey("products.id")),
    Column("option_id", String(255), ForeignKey("characteristic_options.id")),
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

    # old
    #mapper_registry.map_imperatively(
    #    model.PartConfiguration,
    #    part_configuration,
    #    properties={
    #        "id": part_configuration.c.id,
    #        # "product_id": part_configuration.c.product_id,
    #        "part_id": part_configuration.c.part_id,
    #        "available_options": relationship(
    #            model.PartOption,
    #            secondary=part_configuration_options,
    #            # primaryjoin=(part_configuration.c.id == part_configuration_options.c.configuration_id),
    #            # secondaryjoin=(part_configuration_options.c.option_id==part_option.c.id),
    #            collection_class=list,
    #        )
    #    }
    #)

    # new
    # mapper_registry.map_imperatively(
    #     model.PartConfiguration,
    #     properties={
    #     "part_id": part_configuration.c.part_id,
    #         "selected_option": relationship(
    #             model.PartOption,
    #             primaryjoin=(part_configuration.c.option_id == part_option.c.id)
    #         ),
    #         "available_options": relationship(
    #             model.PartOption,
    #             primaryjoin=(part_configuration.c.part_id == product_part.c.id),
    #             secondary=part_option,
    #             collection_class=list
    #         )
    #     }
    # )
    mapper_registry.map_imperatively(
        model.CharacteristicOption,
        characteristic_option,
        properties={
            "id": characteristic_option.c.id,
            "name": characteristic_option.c.name,
            "characteristic_type": characteristic_option.c.type,
            "in_stock": characteristic_option.c.in_stock
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
            #"parts": relationship(model.ProductPart, backref="product"),
            #"part_configs": relationship(model.PartConfiguration, backref="product"),
            # here it should be a list
            "default_characteristics": relationship(
                model.CharacteristicOption, 
                # backref="product", 
                secondary=product_characteristic_options,
                primaryjoin=(product.c.id == product_characteristic_options.c.product_id),
                secondaryjoin=(product_characteristic_options.c.option_id == characteristic_option.c.id),
                collection_class=list
            ),
            #"available_characteristics": relationship(model.CharacteristicOption, backref="product")
            "available_characteristics": relationship(
                model.CharacteristicOption, 
                # backref="product", 
                secondary=product_characteristic_options,
                primaryjoin=(product.c.id == product_characteristic_options.c.product_id),
                secondaryjoin=(product_characteristic_options.c.option_id == characteristic_option.c.id),
                collection_class=list
            ),
        }
    )
