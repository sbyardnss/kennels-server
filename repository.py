DATABASE = {
    "animals": [
        {
            "id": 1,
            "name": "Snickers",
            "species": "Dog",
            "locationId": 1,
            "customerId": 4,
            "status": "Admitted"
        },
        {
            "id": 2,
            "name": "Roman",
            "species": "Dog",
            "locationId": 1,
            "customerId": 2,
            "status": "Admitted"
        },
        {
            "id": 3,
            "name": "Blue",
            "species": "Cat",
            "locationId": 2,
            "customerId": 1,
            "status": "Admitted"
        }
    ],
    "customers": [
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
    ],
    "employees": [
        {
            "id": 1,
            "name": "Jenna Solis"
        }
    ],
    "locations": [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ]
}


def all(resource):
    """For GET requests to collection"""
    if resource == "animals":
        return DATABASE["animals"]
    if resource == "customers":
        return DATABASE["customers"]
    if resource == "employees":
        return DATABASE["employees"]
    if resource == "locations":
        return DATABASE["locations"]


def retrieve(resource, id):
    """For GET requests to a single resource"""
    requested_asset = None
    for asset in DATABASE[resource]:
        if asset["id"] == id:
            requested_asset = asset
    return requested_asset


def create(resource, resource_obj):
    """For POST requests to a collection"""
    max_id = resource[-1]["id"]
    new_id = max_id + 1
    resource_obj["id"] = new_id
    DATABASE[resource].append(resource_obj)
    return resource_obj


def update(resource, new_asset, id):
    """For PUT requests to a single resource"""
    for index, asset in enumerate(DATABASE[resource]):
        if asset["id"] == id:
            DATABASE[resource][index] = new_asset
            break

def delete(resource, id):
    """For DELETE requests to a single resource"""
    asset_index = -1
    for index, asset in enumerate(DATABASE[resource]):
        if asset["id"] == id:
            asset_index = index
    if asset_index >= 0:
        DATABASE[resource].pop(asset_index)

