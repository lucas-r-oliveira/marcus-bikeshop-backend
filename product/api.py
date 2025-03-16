from flask import Blueprint, g

from product.repository import SQLAlchemyProductRepository
from service_layer.product_service import ProductService


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

    @product_bp.route("/bicycles", methods=["GET"])
    def get_bicycle_products():
        service = get_service()

        return service.list_products(), 200

    return product_bp

