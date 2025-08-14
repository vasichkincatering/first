from inventory import Inventory


def test_subrent_request_created_when_stock_insufficient():
    inv = Inventory()
    inv.load_equipment([
        {"name": "excavator", "quantity": 1, "condition": "good", "subrent_cost": 100.0}
    ])
    requests = inv.calculate_requirements({"excavator": 2})
    assert requests and requests[0].item_name == "excavator" and requests[0].quantity == 1
