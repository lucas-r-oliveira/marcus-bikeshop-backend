from dataclasses import dataclass
from typing import Literal
from uuid import uuid4, UUID

from common import Money

class PartOption:
    id: UUID
    name: str
    in_stock: bool = True

    def __init__(self, name: str, in_stock: bool = True):
        self.id = uuid4()
        self.name = name
        self.in_stock = in_stock

    def mark_as_in_stock(self):
        self.in_stock = True

    def mark_as_out_of_stock(self):
        self.in_stock = False

class ProductPart:
    id: UUID
    name: str
    options: list[PartOption] = []


    def __init__(self, name: str, options: list[PartOption] = []): 
        self.id = uuid4()
        self.name = name
        self.options = options

    def add_option(self, name: str, in_stock: bool=True):
        option = PartOption(
            name=name,
            in_stock=in_stock
        )
        
        self.options.append(option)

    def remove_option(self, option_id: UUID):
        self.options = [opt for opt in self.options if opt.id != option_id]

    def get_available_options(self) -> list[PartOption]:
        return [opt for opt in self.options if opt.in_stock]

   
# TODO: review entity vs VO
#class PartConfiguration:
#    id: UUID
#    # product_id: UUID
#    part_name: str
#    part_id: UUID
#    available_options: list[PartOption]
#
#    def __init__(self, 
#                 #product_id: UUID, 
#                 part_id: UUID, 
#                 available_options):
#        self.id = uuid4()
#        self.part_id = part_id
#        # self.product_id = product_id
#        self.available_options = available_options
#        # assert len(self.available_options) >= 1
@dataclass(frozen=True) # should be Frozen=True, its False for compatibility reasons
class PartConfiguration:
    # part_name: str TODO: review
    part_id: UUID
    selected_option: PartOption
    available_options: list[PartOption]

    def __post_init__(self):
        if self.selected_option not in self.available_options:
            raise ValueError("Selected option must be from available options")

type ProductType = Literal["Bicycle"]

type CharacteristicType = Literal[
    "Frame Type", 
    "Frame Finish",
    "Wheels", 
    "Rim Color", 
    "Chain",
    "Size", 
    "Brake Type",
    "Suspension"
] 

@dataclass
class CharacteristicOption:
    id: str #TODO: UUID?
    type: CharacteristicType
    name: str
    in_stock: bool = True
    


class Product:
    id: UUID
    name: str
    description: str
    base_price: Money
    image_url: str
    category: str 
    type: ProductType = "Bicycle" 
    # parts: list[ProductPart] = []
    # part_configs: list[PartConfiguration] = []
    default_characteristics: list[CharacteristicOption]
    available_characteristics: list[CharacteristicOption]

    def __init__(
            self, 
            name: str,
            description: str,
            base_price: Money | float,
            image_url: str,
            category: str,
            part_configs: list[PartConfiguration] = [],
            type: ProductType = "Bicycle",
            parts: list[ProductPart] = [],
            
        ): 
        self.id = uuid4()
        self.name = name
        self.description = description
        if isinstance(base_price, float):
            self.base_price = Money(base_price)
        elif isinstance(base_price, Money):
            self.base_price = base_price
        self.image_url = image_url
        self.category = category
        self.type = type
        self.parts = parts
        self.part_configs = part_configs

    def add_product_part(self, product_part: ProductPart):
        self.parts.append(product_part)

    def remove_product_part(self, product_part_id: UUID):
        
        self.parts = [part for part in self.parts if part.id != product_part_id]
