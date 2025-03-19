import pytest
from config_rules.domain.model import DependencyRule, IncompatibilityRule
from product.domain.model import PartConfiguration, PartOption, Product, ProductPart
from product.repository import InMemoryProductRepository
from config_rules.repository import InMemoryConfigRulesRepository
from orders.repository import InMemoryCartRepository

@pytest.fixture
def in_memory_product_repo():
    return InMemoryProductRepository

@pytest.fixture()
def in_memory_rules_repo():
    return InMemoryConfigRulesRepository

@pytest.fixture()
def in_memory_cart_repo():
    def _create_repo(*args, **kwargs):
        return InMemoryCartRepository(*args, **kwargs)
    return _create_repo

@pytest.fixture
def product_parts():
    wheel_part = ProductPart(name="Wheels")
    wheel_part.add_option("Road Wheels", True)
    wheel_part.add_option("Mountain Wheels", True)
    wheel_part.add_option("Fat Bike Wheels", False)
    wheel_part.add_option("Gravel Wheels", False)

    frame_part = ProductPart(name="Frame") 
    frame_part.add_option("Diamond Frame", True)
    frame_part.add_option("Full-Suspension Frame", False)

    rim_color = ProductPart(name="Rim Color")
    rim_color.add_option("Red Rim Color", True)
    rim_color.add_option("Blue Rim Color", True)

    part_options = []
    for part in [wheel_part, frame_part, rim_color]:
        part_options.extend(part.options)

    return [wheel_part, frame_part, rim_color], part_options

@pytest.fixture
def product(product_parts):
    [parts, options] = product_parts
    product = Product(
        name="Mountain Bike",
        description="A sturdy mountain bike",
        base_price=599.99,
        image_url="https://example.com/bike.jpg",
        category="Mountain Bikes",
        parts=parts,
        part_configs=[
            PartConfiguration(
                part_id=parts[0].id,
                available_options=options[0:3]
            ),
            PartConfiguration(
                part_id=parts[1].id,
                available_options=options[4:6]
            ),
            PartConfiguration(
                part_id=parts[2].id,
                available_options=options[6:-1]
            )
        ]
    )
    return product


@pytest.fixture
def rules(product_parts):
    [_, options] = product_parts

    mountain_wheels: PartOption = [opt for opt in options if opt.name == "Mountain Wheels"][0]
    full_suspension_frame = [opt.id for opt in options if opt.name == "Full-Suspension Frame"]

    mountain_wheels_dep_rule = DependencyRule(
        if_option=mountain_wheels.id,
        then_options=full_suspension_frame,
        error_message="" # TODO:
    )

    fat_bike_wheels: PartOption = [opt for opt in options if opt.name == "Fat Bike Wheels"][0]
    red_rim_color = [opt.id for opt in options if opt.name == "Red Rim Color"]

    fat_bike_wheels_incompat_rule = IncompatibilityRule(
        if_option=fat_bike_wheels.id,
        then_options=red_rim_color,
        error_message="" # TODO:
    )

    return [mountain_wheels_dep_rule, fat_bike_wheels_incompat_rule]
