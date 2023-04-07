CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    },
    {
        "id": 2,
        "name": "Bill Phillips"
    },
    {
        "id": 3,
        "name": "Mary Smith"
    },
    {
        "id": 4,
        "name": "Jennifer Porter"
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

def create_customer(customer):
    """function for creating new customer"""
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    """function for deleting an customer"""
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """function for updating a customer"""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
