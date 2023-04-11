import json
import sqlite3
from models import Location
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
    """sql get all locations"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)
        locations = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)
    return locations

def get_single_location(id):
    """sql single location fetch"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, ( id, ))
        data = db_cursor.fetchone()
        location = Location(data['id'], data['name'], data['address'])
    return location.__dict__


# OLD VERSIONS
# def get_all_locations():
#     """function for viewing all locations"""
#     return LOCATIONS


# def get_single_location(id):
#     """function for getting individual location by id"""
#     requested_location = None

#     for loc in LOCATIONS:
#         if loc["id"] == id:
#             requested_location = loc
#     return requested_location

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


def delete_location(id):
    """function for deleting a location"""
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
    if location_index >= 0:
        LOCATIONS.pop(location_index)


def update_location(id, new_location):
    """function for updating a location"""
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break
