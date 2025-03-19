import pytest
from uuid import uuid4
from service_layer.config_rules_service import ConfigurationRuleService
from service_layer.product_service import ProductService
from service_layer.orders_service import OrdersService
from orders.domain.model import CartItem

from common import Money


# def make_cart_items():
# 
#     product_ids = [uuid4() for _ in range(2)] 
#     part_ids = [uuid4() for _ in range(2)] 
#     option_ids = [uuid4() for _ in range(5)] 
# 
#     # should cart item id be generated in the frontend? no... I dont think so
#     # im not quite surea...
#     # lets assume its not
#     # though the init expects one... so we're forced to assume its created in the frontend
#     # FIXME
# 
#     # however were assuming the cart is
#     cart_item1 = CartItem(
#         id=uuid4(), product_id=product_ids[0], 
#         unit_price=Money(amount=599.99, currency="EUR"), 
#         part_configs=set([{part_ids[0]: option_ids[0], part_ids[1]: option_ids[2]}])
#     )
#     cart_item2 = CartItem(
#         id=uuid4(), product_id=product_ids[1], 
#         unit_price=Money(amount=799.99, currency="EUR"), 
#         part_configs=set([{part_ids[0]: option_ids[1], part_ids[1]: option_ids[2], part_ids[2]: option_ids[4]}])
#     )
#
#    return [cart_item1, cart_item2]


def test_add_to_cart_success(
        product_parts, 
        product, 
        rules,
        in_memory_product_repo, 
        in_memory_rules_repo,
        in_memory_cart_repo
    ):
    [parts, options] = product_parts

    repo = in_memory_cart_repo()


    product_repo = in_memory_product_repo(parts, options, [product])
    product_service = ProductService(product_repo)

    config_rules_repo = in_memory_rules_repo(rules)
    config_rules_service = ConfigurationRuleService(config_rules_repo)

    service = OrdersService(repo, config_rules_service , product_service)

    # for the in memory repo we're assuming one cart only for ease of use
    cart = service.get_cart(uuid4())
    assert len(cart.items) == 0

    options_selection = {
        parts[0].id: parts[0].options[0].id, 
        parts[1].id: parts[1].options[4].id,
        parts[2].id: parts[2].options[6].id
    }
    cart = service.add_to_cart(product.id, cart.id, options_selection) 

    assert len(cart.items) == 1
    assert cart.total_price == Money(599.99)
    assert cart.total_count == 1

    retrieved_cart = repo.get("")
    assert len(retrieved_cart.items) == 1
    assert retrieved_cart.total_price == Money(599.99)
    assert retrieved_cart.total_count == 1


# how can adding to the cart fail?

def test_adding_same_item_existing_cart_increases_qty_and_price(
        in_memory_cart_repo, 
        in_memory_product_repo,
        in_memory_rules_repo,
        product_parts,
        product,
        rules
    ):

    [parts, options] = product_parts
    
    repo = in_memory_cart_repo()

    product_repo = in_memory_product_repo(parts, options, [product])

    config_rules_repo = in_memory_rules_repo(rules)

    product_service = ProductService(product_repo)
    config_rules_service = ConfigurationRuleService(config_rules_repo)

    
    service = OrdersService(repo, config_rules_service, product_service)
    
    cart = service.get_cart(uuid4())

    assert cart.total_price == Money(0)
    assert len(cart.items) == 0
    assert cart.total_count ==0

    options_selection = {
        parts[0].id: parts[0].options[0].id, 
        parts[1].id: parts[1].options[4].id,
        parts[2].id: parts[2].options[6].id
    }

    cart2 = service.add_to_cart(product.id, cart.id, options_selection)
    
    assert cart2.id == cart.id
    assert len(cart2.items) == 1
    assert cart2.total_count == 1 
    assert cart2.total_price == Money(599.99)

    cart3 = service.add_to_cart(product.id, cart.id, options_selection)
    assert cart3.id == cart2.id
    assert len(cart3.items) == 1
    assert cart3.total_count == 2
    assert cart3.total_price == Money(599.99) *2

# TODO: remove from cart
# TODO: clear cart
