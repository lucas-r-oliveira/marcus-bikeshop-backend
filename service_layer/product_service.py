from uuid import UUID

from common import PartConfiguration
from product.domain.model import Product, ProductPart, PartOption
from product.repository import AbstractProductRepository

from config_rules.repository import AbstractConfigRulesRepository

# @dataclass
# class PartOption:
#     id: UUID
#     name: str
#     description: str | None = None
#     in_stock: bool = True

# @dataclass
# class Part:
#     id: UUID
#     name: str 
#     options: list[PartOption]

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
            parts: list[ProductPart] = [], #FIXME: still depends on ProductPart # TODO: review was this mentioning the dataclass or the model
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

    def get_product(self, product_id: UUID) -> Product | None:
        return self.product_repo.get(product_id)

    def list_products(self) -> list[Product]:
        return self.product_repo.get_all()

    # TODO
    def mark_product_part_as_out_of_stock(self):
        pass

    # TODO
    def mark_product_part_as_in_stock(self):
        pass

    def validate_all_configs_are_in_stock(self, configurations: list[PartConfiguration]) -> bool:
        part_options_ids: list[UUID] = [v for config in configurations for v in config.values()]
            
        part_options: list[PartOption] = self.product_repo.get_part_options(ids=part_options_ids)

        return all(part_opt.in_stock for part_opt in part_options)

    #def add_part_option(self, product_id: UUID, product_part_id: UUID, option_name: str, option_in_stock: bool):
    #    product = self.product_repo.get(product_id) #TODO: review, this will probably not work
    #    if not product:
    #        raise ValueError(f"Product id={product_id} was not found")

    #    part_option = PartOption(name=option_name, in_stock=option_in_stock)

    #    product.add_product_part_option()
