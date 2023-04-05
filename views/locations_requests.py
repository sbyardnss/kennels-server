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

def create_location(location):
    """function for creating an location"""
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location
