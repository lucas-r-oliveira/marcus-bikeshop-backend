from uuid import UUID, uuid4
from common import Money, PartOptionSelection

class CartItem:
    id: UUID 
    product_id: UUID
    part_selections: PartOptionSelection
    unit_price: Money
    qty: int = 1


    def __init__(self, product_id: UUID, unit_price: Money, part_selections: PartOptionSelection, qty: int = 1):
        self.id = uuid4()
        self.product_id = product_id
        self.unit_price = unit_price
        self.part_selections = part_selections
        self.qty = qty

    @property
    def total_price(self) -> Money:
        return self.unit_price * self.qty

class Cart:
    id: UUID
    items: list[CartItem]

    def __init__(self, items: list[CartItem] | None= None):
        self.id = uuid4()
        self.items = items if items is not None else []


    def add_item(self, item: CartItem):
        for existing_item in self.items:
            if (existing_item.product_id == item.product_id and
                    existing_item.part_selections == item.part_selections):
                existing_item.qty += item.qty
                return
        
        self.items.append(item)
                
    def remove_item(self, item_id: UUID):
        self.items = [item for item in self.items if item.id != item_id]

    def clear(self):
        self.items = []

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

