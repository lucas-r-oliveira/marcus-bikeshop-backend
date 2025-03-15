from uuid import UUID
from common import Money


class CartItem:
    id: UUID # TODO: review: this is currently being generated in the frontend
    product_id: UUID
    # TODO: Selected Product Config
    unit_price: Money
    image_url: str
    qty: int = 1


    # if we follow exactly what we have in the frontend, 
    # then we need to pass in a cart item id here
    # TODO: review should it be created here?
    def __init__(self, id: UUID, product_id: UUID, unit_price: Money, image_url: str, qty: int = 1):
        self.id = id
        self.product_id = product_id
        self.unit_price = unit_price
        self.image_url = image_url
        self.qty = qty

    @property
    def total_price(self) -> Money:
        return self.unit_price * self.qty

class Cart:
    id: UUID
    # customer_id: 
    items: list[CartItem] = []

    # TODO: id 
    def __init__(self, items: list[CartItem] = []):
        self.items = items


    def add_item(self, item: CartItem):
        for existing_item in self.items:
            if (existing_item.product_id == item.product_id): #and
                #TODO: existing_item.configuration == item.configuration):
                existing_item.qty += item.qty
                return
        
        self.items.append(item)
                
    def remove_item(self, item_id: UUID):
        self.items = [item for item in self.items if item.id != item_id]

    def update_qty(self, item_id: UUID, qty: int):
        for item in self.items:
            if item.id == item_id:
                item.qty = qty
                break

    @property
    def total_price(self) -> Money:
        total = Money(0) 
        for item in self.items:
            total += item.total_price
        return total

    @property
    def total_count(self) -> int:
        return sum(item.qty for item in self.items)

