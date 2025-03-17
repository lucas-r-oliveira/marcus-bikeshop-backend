from uuid import UUID
from common import Money, PartConfiguration




class CartItem:
    id: UUID # TODO: review: this is currently being generated in the frontend
    product_id: UUID
    part_configs: set[PartConfiguration] # set[{part_id: option_id}]  #TODO: review set vs list?
    unit_price: Money
    qty: int = 1


    # if we follow exactly what we have in the frontend, 
    # then we need to pass in a cart item id here
    # TODO: review should it be created here?
    def __init__(self, id: UUID, product_id: UUID, unit_price: Money, part_configs: set[PartConfiguration], qty: int = 1):
        self.id = id
        self.product_id = product_id
        self.unit_price = unit_price
        self.part_configs = part_configs
        self.qty = qty

    @property
    def total_price(self) -> Money:
        return self.unit_price * self.qty

class Cart:
    id: UUID
    user_id: UUID | None = None
    items: list[CartItem] = []

    # If we assume the cart_id always comes from the frontend,
    # then it necessarily have to receive an id here.
    # it cant be None
    def __init__(self, id: UUID,  items: list[CartItem] = []):
        self.id = id
        self.items = items


    def add_item(self, item: CartItem):
        for existing_item in self.items:
            if (existing_item.product_id == item.product_id and
                    existing_item.part_configs == item.part_configs):
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

