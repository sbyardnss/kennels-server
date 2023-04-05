CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

def get_all_customers():
    """function for viewing all customers"""
    return CUSTOMERS


def get_single_customer(id):
    """function for getting individual customer by id"""
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer
