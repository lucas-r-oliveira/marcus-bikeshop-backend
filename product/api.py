from uuid import UUID
from product.repository import SQLAlchemyProductRepository
from service_layer.product_service import ProductService
from common import Money, PartOptionSelection

from flask import Blueprint, g 
from flask_pydantic_api.api_wrapper import pydantic_api
from pydantic import BaseModel, field_serializer


class PartOptionResponse(BaseModel):
    id: UUID
    name: str
    in_stock: bool

    class Config:
        from_attributes=True

class ProductPartResponse(BaseModel):
    id: UUID
    name: str
    options: list[PartOptionResponse]

    class Config:
        from_attributes=True

class PartConfigurationResponse(BaseModel):
    id: UUID
    part_id: UUID
    available_options: list[PartOptionResponse]

    class Config:
        from_attributes=True

class ProductResponse(BaseModel):
    id: UUID
    name: str
    description: str
    base_price: Money
    currency: Money = Money(0, currency="EUR")
    image_url: str
    category: str
    parts: list[ProductPartResponse]
    part_configs: list[PartConfigurationResponse]
    # type

    class Config:
        from_attributes=True

    @field_serializer("base_price")
    def serialize_base_price(self, money: Money):
        return money.amount

    @field_serializer("currency")
    def serialize_currency(self, money: Money):
        return money.currency

class CreateProductRequest(BaseModel):
    name: str
    description: str
    base_price: float
    currency: str
    image_url: str
    category: str
    parts: list[PartOptionSelection]  
    # type


def create_product_bp(session_factory):
    product_bp = Blueprint('product', __name__, url_prefix="/products")

    @product_bp.before_request
    def before_request():
        g.db_session = session_factory()

    @product_bp.teardown_request
    def teardown_request(exception=None):
        g.db_session.close()

    def get_service():
        product_repo = SQLAlchemyProductRepository(g.db_session)
        return ProductService(product_repo)

    #---- ADD YOUR ROUTES HERE ------------------

    @product_bp.get("/bicycles") # type: ignore
    @pydantic_api(
        name="Get all bicycle products",
        tags=["products", "bicycles"],
        success_status_code=200,
    )
    def get_all_bicycle_products() -> list[ProductResponse]: 
        service = get_service()
        products = service.list_products()

        # return [
        #     ProductResponse(
        #         id=product.id, 
        #         name=product.name, 
        #         description=product.description, 
        #         base_price=product.base_price.amount, 
        #         currency=product.base_price.currency, 
        #         image_url=product.image_url,
        #         parts=product.parts, 
        #         part_configs=product.part_configs, #type: ignore
        #         category=product.category
        #     ).model_dump() for product in service.list_products()
        # ]

        return [ProductResponse.model_validate(product).model_dump() for product in products]

    @product_bp.post("/bicycles") # type: ignore
    @pydantic_api(
        name="Create a bicycle product",
        tags=["products", "bicycles"],
        success_status_code=201,
    )
    def post_bicycle_product(body: CreateProductRequest) -> ProductResponse: 
        service = get_service()

        # TODO: parts
        # TODO: part_configs
        # TODO: type
        product = service.create_product(

            name=body.name,
            description=body.description,
            base_price=body.base_price,
            image_url=body.image_url,
            category=body.category,
        )

        return ProductResponse(
            id=product.id, 
            name=product.name, 
            description=product.description, 
            base_price=product.base_price, #type: ignore
            currency=product.base_price, #type: ignore
            image_url=product.image_url,
            # parts=product.parts,
            category=product.category
        ) 



    return product_bp

