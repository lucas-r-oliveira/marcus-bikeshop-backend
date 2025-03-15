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

   
type ProductType = Literal["Bicycle"]

class Product:
    # aggregate or not?
    id: UUID
    name: str
    description: str
    base_price: Money
    image_url: str
    category: str 
    type: ProductType = "Bicycle" 
    parts: list[ProductPart] = []

    def __init__(
            self, 
            name: str,
            description: str,
            base_price: Money,
            image_url: str,
            category: str,
            type: ProductType = "Bicycle",
            parts: list[ProductPart] = []
        ): 
        self.id = uuid4()
        self.name = name
        self.description = description
        self.base_price = base_price
        self.image_url = image_url
        self.category = category
        self.type = type
        self.parts = parts

    def add_product_part(self, product_part: ProductPart):
        self.parts.append(product_part)

    def remove_product_part(self, product_part_id: UUID):
        self.parts = [part for part in self.parts if part.id != product_part_id]
