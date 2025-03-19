from uuid import UUID

from orders.domain.model import Cart, CartItem
from orders.repository import AbstractCartRepository
from service_layer.product_service import ProductService
from service_layer.config_rules_service import ConfigurationRuleService

from common import PartOptionSelection

class OrdersService:
    cart_repo: AbstractCartRepository
    config_rules_service: ConfigurationRuleService
    product_service: ProductService

    def __init__(
            self, 
            cart_repo: AbstractCartRepository, 
            config_rules_service: ConfigurationRuleService,
            product_service: ProductService

        ):
        self.cart_repo = cart_repo
        self.config_rules_service = config_rules_service
        self.product_service = product_service

    def get_cart(self, cart_id: UUID):
        cart = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart()
            self.cart_repo.create_or_update(cart)

        return cart

    def add_to_cart(self, product_id: UUID, cart_id: UUID, selections: PartOptionSelection) -> Cart: 
        cart = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart()
            self.cart_repo.create_or_update(cart)
        
        valid = self.product_service.validate_all_selections_are_in_stock(selections) 
        if not valid:
            raise ValueError("At least one part option is out of stock.")

        success, err_msg = self.config_rules_service.validate_selections(selections=selections)
        if not success:
            raise ValueError(err_msg)

        product = self.product_service.get_product(product_id)
        if not product:
            raise ValueError(f"Product <{product_id=}> was not found.")

        cart_item = CartItem(
            product_id=product_id, 
            unit_price=product.base_price, 
            part_selections=selections
        )


        cart.add_item(cart_item)
        cart = self.cart_repo.create_or_update(cart)

        return cart

    def remove_from_cart(self, cart_id: UUID, cart_item_id: UUID) -> Cart:
        cart = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart(id=cart_id)
        cart.remove_item(cart_item_id)

        return self.cart_repo.create_or_update(cart)

    def update_cart_item_qty(self, cart_id: UUID, cart_item_id: UUID, qty: int) -> Cart:
        cart: Cart | None = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart(id=cart_id)
            # log(f"Cart <{cart_id=}> was not found. Not enough information to proceed")
            return self.cart_repo.create_or_update(cart)

        cart.update_qty(cart_item_id, qty)
        return self.cart_repo.create_or_update(cart)

    def clear_cart(self, cart_id: UUID):
        cart: Cart | None = self.cart_repo.get(cart_id)
        if not cart:
            cart = Cart(id=cart_id)
            return self.cart_repo.create_or_update(cart)

        cart.clear()
        return self.cart_repo.create_or_update(cart)

