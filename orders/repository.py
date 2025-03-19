from abc import abstractmethod, ABC
from orders.domain.model import Cart, CartItem

from sqlalchemy import text

class AbstractCartRepository(ABC):
    @abstractmethod
    def create_or_update(self, cart: Cart) -> Cart:
        raise NotImplementedError

    @abstractmethod
    def get(self, cart_id) -> Cart | None:
        raise NotImplementedError

    @abstractmethod
    def get_cart_item(self, cart_id, cart_item_id) -> CartItem | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Cart]:
        raise NotImplementedError


class SQLAlchemyCartRepository(AbstractCartRepository):
    def __init__(self, session):
        self.session = session

    def create_or_update(self, cart: Cart) -> Cart:
        return self.session.merge(cart)

    def get(self, cart_id) -> Cart | None:
        return self.session.query(Cart).filter_by(id=cart_id).one_or_none()

    def get_cart_item(self, cart_id, cart_item_id) -> CartItem | None:
        table_name = "cart_items"
        query = text(f"SELECT * FROM {table_name} WHERE cart_id = :cart_id and id = :id")

        return self.session.execute(query, {"cart_id": cart_id, "id": cart_item_id}).fetchall()

    def get_all(self):
        return self.session.query(Cart).all() or []

class InMemoryCartRepository(AbstractCartRepository):
    def __init__(self, cart=None, cart_items=None):

        self._cart = cart if cart is not None else Cart()
        self._cart_items = set(cart_items if cart_items is not None else [])

    def create_or_update(self, cart):
        self._cart = cart
        return self._cart
        

    def get(self, cart_id):
        return self._cart

    def get_cart_item(self, cart_id, cart_item_id): 
        for item in self._cart_items:
            if item.id == cart_item_id:
                return item

    def get_all(self) -> list[Cart]:
        return [self._cart]
