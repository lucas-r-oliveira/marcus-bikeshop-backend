from dataclasses import dataclass
from uuid import UUID

from product.domain.model import Product, ProductPart
from product.repository import AbstractProductRepository

from config_rules.repository import AbstractConfigRulesRepository

@dataclass
class PartOption:
    id: UUID
    name: str
    description: str | None = None
    in_stock: bool = True

@dataclass
class Part:
    id: UUID
    name: str 
    options: list[PartOption]

class ProductService:
    product_repo: AbstractProductRepository
    config_rules_repo: AbstractConfigRulesRepository

    def __init__(self, product_repo: AbstractProductRepository):
        self.product_repo = product_repo

    def create_product(
            self, 
            name: str, 
            description: str, 
            base_price: float,
            image_url: str,
            category: str,
            # type: str,
            parts: list[ProductPart] = [], #FIXME: still depends on ProductPart
        ) -> Product:

        product = Product(
            name=name, 
            description=description, 
            base_price=base_price, 
            image_url=image_url, 
            category=category, 
            parts=parts
        )

        self.product_repo.add(product)
        return product

    def get_product(self, product_id: UUID) -> Product:
        return self.product_repo.get(product_id)

    def list_products(self) -> list[Product]:
        return self.product_repo.list()


    #def add_part_option(self, product_id: UUID, product_part_id: UUID, option_name: str, option_in_stock: bool):
    #    product = self.product_repo.get(product_id) #TODO: review, this will probably not work
    #    if not product:
    #        raise ValueError(f"Product id={product_id} was not found")

    #    part_option = PartOption(name=option_name, in_stock=option_in_stock)

    #    product.add_product_part_option()

    def validate_configuration(self, product_id: UUID, config: dict) -> tuple[bool, str | None]:
        product = self.get_product(product_id)
        if not product:
            return False, f"Product <{product_id=}> not found"

        # check stock?
        # check required?

        # check product-specific config rules
        rules = self.config_rules_repo.get_rules_for_product(product_id)
        for rule in rules:
            if not rule.validate(config):
                return False, rule.error_message

        return True, None

