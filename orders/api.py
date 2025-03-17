from uuid import UUID

from common import Money, PartConfiguration
from config_rules.repository import SQLAlchemyConfigRulesRepository
from orders.repository import SQLAlchemyCartRepository
from product.repository import SQLAlchemyProductRepository
from service_layer.config_rules_service import ConfigurationRuleService
from service_layer.product_service import ProductService
from service_layer.orders_service import OrdersService

from flask import Blueprint, g 
from flask_pydantic_api.api_wrapper import pydantic_api
from pydantic import BaseModel, field_serializer


class AddToCartRequest(BaseModel):
    product_id: UUID
    configurations: list[PartConfiguration]
    # TODO: review nothing else?

    # @field_serializer('configurations')
    # def serialize_configurations(self, configurations):
    #     return [
    #         {UUID(part_id): UUID(option_id) for part_id, option_id in config.items()}
    #         for config in configurations
    #     ]

class UpdateCartItemQtyRequest(BaseModel):
    qty: int

class CartItemResponse(BaseModel):
    id: UUID
    product_id: UUID
    part_configs: set[PartConfiguration]

    unit_price: float
    qty: int

    @field_serializer('unit_price')
    def serialize_unit_price(self, unit_price: Money) -> float:
        return unit_price.amount


class CartResponse(BaseModel):
    id: UUID
    items: list[CartItemResponse]


def create_orders_bp(session_factory):
    orders_bp = Blueprint('orders', __name__)

    @orders_bp.before_request
    def before_request():
        g.db_session = session_factory()

    @orders_bp.teardown_request
    def teardown_request(exception=None):
        g.db_session.close()

    def get_service():
        cart_repo = SQLAlchemyCartRepository(g.db_session)
        product_repo = SQLAlchemyProductRepository(g.db_session)
        rule_repo = SQLAlchemyConfigRulesRepository(g.db_session)

        config_rules_service = ConfigurationRuleService(rule_repo)
        product_service = ProductService(product_repo)
        return OrdersService(cart_repo, config_rules_service, product_service)

    #---- ADD YOUR ROUTES HERE ------------------

    @orders_bp.get("/cart/<uuid:cart_id>") # type: ignore
    @pydantic_api(
        name="Get cart",
        tags=["orders", "cart"],
        success_status_code=200,
    )
    def get_cart(cart_id: UUID) -> CartResponse:
        service = get_service()

        cart = service.get_cart(cart_id)
        
        cart_items = [
            CartItemResponse(
                id=item.id,
                product_id=item.product_id,
                part_configs=item.part_configs,
                unit_price=item.unit_price, #type: ignore
                qty=item.qty
            ) for item in cart.items
        ]

        return CartResponse(id=cart.id, items=cart_items)


    @orders_bp.post("/cart/<uuid:cart_id>/items") # type: ignore
    @pydantic_api(
        name="Add item to cart",
        tags=["orders", "cart"],
        success_status_code=201,
    )
    def add_to_cart(cart_id: UUID, body: AddToCartRequest) -> CartResponse:
        service = get_service()
        
        cart = service.add_to_cart(
            product_id=body.product_id,
            cart_id=cart_id,
            configurations=body.configurations 
        )
        
        cart_items = [
            CartItemResponse(
                id=item.id, 
                product_id=item.product_id, 
                part_configs=item.part_configs,
                unit_price=item.unit_price,  #type: ignore
                qty=item.qty
            ) for item in cart.items
        ]
        
        return CartResponse(id=cart.id, items=cart_items)

    @orders_bp.delete("/cart/<uuid:cart_id>/items/<uuid:item_id>") # type: ignore
    @pydantic_api(
        name="Remove item from cart",
        tags=["orders", "cart"],
        success_status_code=200,
    )
    def remove_from_cart(cart_id: UUID, item_id: UUID) -> CartResponse:
        service = get_service()
        cart = service.remove_from_cart(cart_id, item_id)
        
        cart_items = [
            CartItemResponse(
                id=item.id, 
                product_id=item.product_id,
                part_configs=item.part_configs,
                unit_price=item.unit_price, #type: ignore
                qty=item.qty
            ) for item in cart.items
        ]
        
        return CartResponse(id=cart.id, items=cart_items) 
    
    @orders_bp.patch("/cart/<uuid:cart_id>/items/<uuid:item_id>") # type: ignore
    @pydantic_api(
        name="Update cart item quantity",
        tags=["orders", "cart"],
        success_status_code=200,
    )
    def update_cart_item_qty(cart_id: UUID, item_id: UUID, body: UpdateCartItemQtyRequest) -> CartResponse:
        service = get_service()
        cart = service.update_cart_item_qty(cart_id, item_id, body.qty)
        
        cart_items = [
            CartItemResponse(
                id=item.id, 
                product_id=item.product_id,
                part_configs=item.part_configs,
                unit_price=item.unit_price, # type: ignore
                qty=item.qty
            ) for item in cart.items
        ]
        
        return CartResponse(id=cart.id, items=cart_items) 

    return orders_bp
