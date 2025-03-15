from dataclasses import dataclass, field
from uuid import uuid4, UUID
from typing import Literal

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "EUR"

    def __add__(self, other):
        if (self.currency != other.currency):
            raise ValueError("Cannot add different currencies together")
        return Money(self.amount + other.amount, self.currency)


    
# if I keep the "value" property, I can just make this into an ID Class
# and inherit from it, but I dont really like id.value
@dataclass(frozen=True)
class PartOptionId:
    value: UUID = field(default_factory=uuid4)

@dataclass(frozen=True)
class ProductPartId:
    value: UUID = field(default_factory=uuid4)

@dataclass(frozen=True)
class ProductId:
    value: UUID = field(default_factory=uuid4)


class PartOption:
    id: PartOptionId
    name: str
    in_stock: bool = True

    def __init__(self, name: str, in_stock: bool = True):
        self.name = name
        self.in_stock = in_stock

    def mark_as_in_stock(self):
        self.in_stock = True

    def mark_as_out_of_stock(self):
        self.in_stock = False

class ProductPart:
    id: ProductPartId
    name: str
    options: list[PartOption] = []


    def __init__(self, name: str, options: list[PartOption] = []): 
        self.name = name
        self.options = options

   
type ProductType = Literal["Bicycle"]

class Product:
    # aggregate or not?
    id: ProductId
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
        self.name = name
        self.description = description
        self.base_price = base_price
        self.image_url = image_url
        self.category = category
        self.type = type
        self.parts = parts

