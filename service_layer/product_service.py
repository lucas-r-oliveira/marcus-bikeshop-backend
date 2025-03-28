from typing import NotRequired, TypedDict
from uuid import UUID

from common import PartOptionSelection
from product.domain.model import Product, ProductPart, PartOption
from product.repository import AbstractProductRepository

from config_rules.repository import AbstractConfigRulesRepository

class PartOptionDict(TypedDict):
    id: NotRequired[UUID]
    name: str
    in_stock: bool

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

    def delete_product(self, product_id: UUID):
        try:
            self.product_repo.remove(product_id)
        except Exception as e:
            raise

    def get_product(self, product_id: UUID) -> Product | None:
        return self.product_repo.get(product_id)

    def list_products(self) -> list[Product]:
        return self.product_repo.get_all()

    def create_part(self, name: str, options: list[PartOptionDict]) -> ProductPart:
        if len(options) == 0:
            raise ValueError(f"Error when trying to create part <{name=}> To create a product part you need to provide at least one option.")

        part_options = [] #set()
        part_options.extend([PartOption(name=opt.get("name"), in_stock=opt.get("in_stock", True)) for opt in options])
        
        part = ProductPart(name, part_options)
        # TODO: part should come from the add/create operation, otherwise we can be working
        # with an object thats in memory but not in db (if something fails)
        self.product_repo.create_part(part)

        return part

    def get_part(self, part_id: UUID) -> ProductPart | None:
        return self.product_repo.get_part(part_id)


    def set_available_part_configs(self, product_id: UUID, configs: dict[UUID, list[UUID]]) -> Product: 
        product = self.get_product(product_id)
        if not product:
            raise ValueError(f"Product id={product_id} was not found.")

        
        # I have two options here (and across the rest of the service)
        # 1. do it directly in the repo and return prroduct
        # 2. do it in the domain object and call repo.update(product) or something similar
        # update product in db # TODO:
        product = self.product_repo.set_available_part_configs(product.id, configs)

        return product


    def mark_part_option_as_out_of_stock(self, option_id: UUID):
        part_options: list[PartOption] = self.product_repo.get_part_options(ids=[option_id])
        if not part_options:
            raise ValueError(f"Part Option id={option_id} was not found.")

        part_option = part_options[0]
        # see, here we're doing the opposite approach from below
        # its not consistent
        # TODO: review workflow

        part_option.mark_as_out_of_stock()
        self.product_repo.update_part_option(part_option)


    def mark_part_option_as_in_stock(self, option_id: UUID):
        part_options: list[PartOption] = self.product_repo.get_part_options(ids=[option_id])
        if not part_options:
            raise ValueError(f"Part Option id={option_id} was not found.")

        part_option = part_options[0]
        # see, here we're doing the opposite approach from below
        # its not consistent
        # TODO: review workflow

        part_option.mark_as_in_stock()
        self.product_repo.update_part_option(part_option)

    def validate_all_selections_are_in_stock(self, selections: PartOptionSelection) -> bool:
        part_options_ids: list[UUID] = list(selections.values())
            
        part_options: list[PartOption] = self.product_repo.get_part_options(ids=part_options_ids)

        return all(part_opt.in_stock for part_opt in part_options)

    # is there any actual difference between these two?
    def create_part_option(self):
        pass

    def add_part_option(self, product_id: UUID, product_part_id: UUID, option_name: str, option_in_stock: bool):
        # lets assume here the option already exists and we're just linking iot
        product = self.product_repo.get(product_id)
        if not product:
            raise ValueError(f"Product id={product_id} was not found")

        # part_option = PartOption(name=option_name, in_stock=option_in_stock)

        # it can either
        # I would guess this one just adds an existing option, hence requiring the option_id also

        # product.add_product_part_option()
