from flask import Blueprint, g 
from flask_pydantic_api.api_wrapper import pydantic_api

from product.repository import SQLAlchemyProductRepository
from service_layer.product_service import ProductService


from pydantic import BaseModel


class PartOptionAPI(BaseModel):
    id: str
    name: str
    in_stock: bool

class ProductPartAPI(BaseModel):
    id: str
    name: str
    options: list[PartOptionAPI]

class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    base_price: float
    currency: str
    image_url: str
    category: str
    # parts: list[ProductPartAPI]
    # parts
    # type

class CreateProductRequest(BaseModel):
    name: str
    description: str
    base_price: float
    currency: str
    image_url: str
    category: str
    parts: list[dict[str, str]]
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
    def get_bicycle_products() -> list[dict]:#list[ProductResponse]: #FIXME:
        service = get_service()

        return [
            ProductResponse(
                id=str(product.id), 
                name=product.name, 
                description=product.description, 
                base_price=product.base_price.amount,
                currency=product.base_price.currency,
                image_url=product.image_url,
                # parts=product.parts,
                category=product.category
            ).model_dump() for product in service.list_products()
        ]

    @product_bp.post("/bicycles") # type: ignore
    @pydantic_api(
        name="Create a bicycle product",
        tags=["products", "bicycles"],
        success_status_code=201,
    )
    def post_bicycle_product(body: CreateProductRequest) -> ProductResponse: 
        service = get_service()

        # TODO: parts
        # TODO: type
        product = service.create_product(

            name=body.name,
            description=body.description,
            base_price=body.base_price,
            image_url=body.image_url,
            category=body.category,
        )

        return ProductResponse(
            id=str(product.id), 
            name=product.name, 
            description=product.description, 
            base_price=product.base_price.amount,
            currency=product.base_price.currency,
            image_url=product.image_url,
            # parts=product.parts,
            category=product.category
        ) 



    return product_bp

