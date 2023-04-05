LOCATIONS = [
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


def get_all_locations():
    """function for viewing all locations"""
    return LOCATIONS


def get_single_location(id):
    """function for getting individual location by id"""
    requested_location = None

    for loc in LOCATIONS:
        if loc["id"] == id:
            requested_location = loc
    return requested_location
