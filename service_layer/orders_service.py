from uuid import UUID

from orders.domain.model import Cart, CartItem
from orders.repository import AbstractCartRepository
from product.repository import AbstractProductRepository
from service_layer.config_rules_service import ConfigurationRuleService

class OrdersService:
    cart_repo: AbstractCartRepository
    product_repo: AbstractProductRepository
    config_rules_service: ConfigurationRuleService

    def __init__(
            self, 
            cart_repo: AbstractCartRepository, 
            product_repo: AbstractProductRepository,
            config_rules_service: ConfigurationRuleService

        ):
        self.cart_repo = cart_repo
        self.config_rules_service = config_rules_service
        self.product_repo = product_repo

    # hard requirement:  **The user shouldn’t be able to add to cart with a forbidden combination of options or out of stock parts.**
    #TODO: user_id. handle it somehow
    def add_to_cart(self, product_id: UUID, cart_id: UUID, configurations: list[dict[UUID, UUID]]) -> Cart: #user_id: UUID) -> Cart:
        # assume we get a customer/user_id

        # get their cart - to simplify Im going to assume cart_id is created in the frontend, stored and sent to the backend
        cart = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart()
            self.cart_repo.add(cart)
        
        # TODO: validate out of stock parts
        success, err_msg = self.config_rules_service.validate_configurations(product_id=product_id, configurations=configurations)
        if not success:
            raise ValueError(err_msg)

        # create cart item
        product = self.product_repo.get(product_id)
        if not product:
            raise ValueError(f"Product <{product_id=}> was not found")

        # FIXME: id
        cart_item = CartItem(id='', product_id=product_id, unit_price=product.base_price, part_configs=set(configurations))


        # add to cart
        cart.add_item(cart_item)
        cart = self.cart_repo.create_or_update(cart)

        return cart

    def remove_from_cart(self, cart_id: UUID, cart_item_id: UUID) -> Cart:
        cart = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart()
        cart.remove_item(cart_item_id)

        return self.cart_repo.create_or_update(cart_id, cart_item_id)

    def update_cart_item_qty(self, cart_id: UUID, cart_item_id: UUID, qty: int) -> Cart:
        cart: Cart = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart()
            # log(f"Cart <{cart_id=}> was not found. Not enough information to proceed")
            return self.cart_repo.create_or_update(cart)

        cart.update_qty(cart_item_id, qty)
        return self.cart_repo.create_or_update(cart)

    def clear_cart(self, cart_id: UUID):
        cart: Cart = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart()
            return self.cart_repo.create_or_update(cart)

        cart.clear()
        return self.cart_repo.create_or_update(cart)

