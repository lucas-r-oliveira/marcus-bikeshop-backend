from abc import abstractmethod, ABC

from orders.domain.model import Cart, CartItem

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
    def list(self) -> list[Cart]:
        raise NotImplementedError


class SQLAlchemyCartRepository(AbstractCartRepository):
    # TODO: review rollbacks
    def __init__(self, session):
        self.session = session

    def create_or_update(self, cart: Cart) -> Cart:
        # TODO:
        pass

    def get(self, cart_id) -> Cart | None:
        return self.session.query(Cart).filter_by(id=cart_id).one_or_none()

    def get_cart_item(self, cart_id, cart_item_id) -> CartItem | None:
        # TODO: 
        # return self.session.query(Cart).filter_by(reference=cart_id).one_or_none()
        pass

    def list(self):
        return self.session.query(Cart).all() or []
