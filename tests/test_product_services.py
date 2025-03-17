import pytest
from uuid import UUID
from service_layer.product_service import ProductService
from product.repository import AbstractProductRepository
from product.domain.model import ProductPart

class InMemoryProductRepository(AbstractProductRepository):
    def __init__(self, part_options, product_parts, products):
        # TODO: review - do we actually need to pass in part options here? I feel like 
        # we 're doing redundant work

        # we can just extend from product_parts
        self._part_options = set(part_options)
        self._products_parts = set(product_parts)
        self._products = set(products)

    def add(self, product):
        self._products.add(product)

    def get(self, product_id):
        return next(p for p in self._products if p.id == product_id)

    def get_all(self): 
        return list(self._products)

    def get_part_options(self, ids): 
        return list(filter(lambda opt: opt.id in ids, self._part_options))

    def create_part(self, part: ProductPart):
        self._products_parts.add(part)
        self._part_options.update(part.options)

    def get_part(self, part_id):
        for p in self._products_parts:
            if p.id == part_id:
                return p
        

def make_products_parts():
    wheel_part = ProductPart(name="Wheels")
    wheel_part.add_option("26 inch", True)
    wheel_part.add_option("29 inch", True)
    wheel_part.add_option("24 inch", False)

    frame_part = ProductPart(name="Frame")
    frame_part.add_option("Aluminium", True)
    frame_part.add_option("Carbon", False)

    part_options = []
    for part in [wheel_part, frame_part]:
        part_options.extend(part.options)

    return [wheel_part, frame_part], part_options
        
def test_create_product():
    parts, options = make_products_parts()
    repo = InMemoryProductRepository(options, parts, [])
    service = ProductService(repo)

    product = service.create_product(
        name="Mountain Bike",
        description="A sturdy mountain bike",
        base_price=599.99,
        image_url="https://example.com/bike.jpg",
        category="Mountain Bikes",
        # TODO: review parts - we shouldnt necessarily pass domain models here... maybe PartConfigurations or option ids
        parts=parts,
    )

    assert product.id is not None and isinstance(product.id, UUID)
    assert product.name == "Mountain Bike"
    assert product.description == "A sturdy mountain bike"
    assert product.base_price.amount == 599.99 # this should be handled with Decimal 
    assert product.image_url == "https://example.com/bike.jpg"
    assert product.category == "Mountain Bikes"
    assert len(product.parts) == 2

    retrieved_product = service.get_product(product.id)
    assert retrieved_product is not None
    assert retrieved_product.id == product.id

def test_create_product_part():
    # creating a product part necessarily requires at least one option.
    repo = InMemoryProductRepository([], [], [])
    service = ProductService(repo)

    part = service.create_part(
        name="Frame",
        options=[
            {
                "name": "Full-suspension",
                "in_stock": True,
            },
            {
                "name": "Diamond",
                "in_stock": True,
            },
            {
                "name": "Step-through",
                "in_stock": True,
            },
        ]
    )

    assert part.id is not None and isinstance(part.id, UUID)
    assert part.name == "Frame"
    assert len(part.options) == 3
    assert all(opt.id is not None for opt in part.options)

    retrieved_part = service.get_part(part.id)
    assert retrieved_part is not None
    assert retrieved_part.id == part.id


@pytest.mark.skip
def test_cannot_create_product_part_without_options():
    # you technically can.. and its easier for me part.add_option()
    # but I might change that to include at least one option
    pass
