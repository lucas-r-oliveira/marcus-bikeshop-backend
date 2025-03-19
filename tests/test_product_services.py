import pytest
from uuid import UUID
from service_layer.product_service import ProductService
from common import Money


def test_create_product(product_parts, in_memory_product_repo):
    [parts, options] = product_parts
    repo = in_memory_product_repo(options, parts, [])
    service = ProductService(repo)

    product = service.create_product(
        name="Mountain Bike",
        description="A sturdy mountain bike",
        base_price=599.99,
        image_url="https://example.com/bike.jpg",
        category="Mountain Bikes",
        parts=parts,
        # TODO: part_configs
    )

    assert product.id is not None and isinstance(product.id, UUID)
    assert product.name == "Mountain Bike"
    assert product.description == "A sturdy mountain bike"
    assert product.base_price == Money(599.99) 
    assert product.image_url == "https://example.com/bike.jpg"
    assert product.category == "Mountain Bikes"
    assert len(product.parts) == 3

    retrieved_product = service.get_product(product.id)
    assert retrieved_product is not None
    assert retrieved_product.id == product.id
    assert len(retrieved_product.parts) == 3
    # len part options?

def test_create_product_part(in_memory_product_repo):
    # creating a product part necessarily requires at least one option.
    # this repeating part should be put in a fixture
    repo = in_memory_product_repo([], [], [])
    service = ProductService(repo)

    part = service.create_part(
        name="Frame",
        options=[
            {
                "name": "Full-Suspension Frame",
                "in_stock": True,
            },
            {
                "name": "Diamond Frame",
                "in_stock": True,
            },
            {
                "name": "Step-Through Frame",
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
    assert len(retrieved_part.options) == 3



@pytest.mark.skip
def test_cannot_create_product_part_without_options():
    # you technically can.. and its easier for me part.add_option()
    # but I might change that to include at least one option
    pass

# analogous:  
# not quite sure about this one
@pytest.mark.skip 
def test_cannot_create_product_without_at_least_one_available_config():
    # you technically can.. and its easier for me part.add_option()
    # but I might change that to include at least one option
    pass

# delete is a whole section of its own
# - delete product but parts are being used someplace else, delete just product
# - actually even if its used nowhere else we still might want to keep the parts
# - deleting a part, however, deletes all of its options
# - deleting an option delets the product part if it is the last one standing

# test cannot add repeated_option to part (technically we can, so fix)

# differences between create_part_option and add_part_option/link?
@pytest.mark.skip
def test_create_part_option():
    # for create_part_option we just need a product_part id.
    # for add_part_option we need a product_id
    # so here, we dont actually need the product
    # What we actually need is a part
    # product = make_product()
    # parts, _ = make_product_parts()
    # repo = in_memory_product_repo([], parts, [])
    # service = ProductService(repo)


    # part_option = service.create_part_option(
    #     part_id=parts[0].id,
    #     name="Gravel wheels",
    #     in_stock=True
    # )
    pass

@pytest.mark.skip
def test_configure_part_options_per_product(product_parts, product, in_memory_product_repo):
    [_, options] = product_parts
    repo = in_memory_product_repo([], [], [product])
    service = ProductService(repo)

    product = service.set_available_part_configs(product_id=product.id, configs={
        product.parts[0].id: [
            product.parts[0].options[0].id, 
            product.parts[0].options[1].id
        ]})


    assert product.part_configs == {
        product.parts[0].id: [options[0],options[1]]
    }


    retrieved_product = service.get_product(product.id)
    assert retrieved_product is not None
    # assert len(retrieved_product.available_part_configs[product.parts[0].id]) == 2 -> Why is this failing?
    assert retrieved_product.part_configs == {
        product.parts[0].id: [options[0],options[1]]
    }
    

    # TODO
    # product = service.update_available_part_configs({product.parts[0].id: [product.parts[0].options[2].id]})

    # assert product.part_configs == {
    #     product.parts[0].id: [options[0], options[1], options[2]]
    # }

    # retrieved_product = service.get_product(product.id)
    # assert retrieved_product is not None
    # # assert len(retrieved_product.available_part_configs[product.parts[0].id]) == 3 -> same here
    # assert retrieved_product.part_configs == {
    #     product.parts[0].id: [options[0], options[1], options[2]]
    # }
    

@pytest.mark.skip
def test_mark_part_option_as_out_of_stock(product, product_parts, in_memory_product_repo):
    [parts, options] = product_parts()
    repo = in_memory_product_repo(options, parts, [product])
    service = ProductService(repo)

    # to test here, making one part option OoS makes it so in all products' (including available_part_configs)


    service.mark_part_option_as_out_of_stock(options[0].id)

    assert not options[0].in_stock

    product_with_oos_option = repo.get(product_id=product.id)

    # To check, which might fail...
    # does product have the option set to OoS ?
    # assert
    # if all the
    # assert product.instock


@pytest.mark.skip
def test_mark_part_option_as_in_stock():
    pass

@pytest.mark.skip
def test_all_available_options_out_of_stock_for_given_product_part_make_product_out_of_stock():
    pass

