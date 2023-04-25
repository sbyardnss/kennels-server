from .locations_requests import get_single_location
from . customer_requests import get_single_customer
from models import Customer, Animal, Location
import sqlite3
import json
ANIMALS = [
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
]


def get_all_animals(query):
    # Open a connection to the database
    """sql friendly function for getting all animals"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""
        where_clause = ""
        if len(query) != 0:
            # param = query[0]
            
            # [qs_key, qs_value] = param.split("=")
            # if qs_key == "_sortBy":
            #     if qs_value[0] == 'location':
            #         sort_by = " ORDER BY location_id"
            #     if qs_value[0] == "customer":
            #         sort_by = " ORDER BY customer_id"
            #     if qs_value[0] == 'status':
            #         sort_by = " ORDER BY a.status desc"
            #     if qs_value[0] == "name":
            #         sort_by = " ORDER BY a.name"
            # if qs_key == "locationId":
            #     where_clause = f"WHERE l.id = {qs_value}"
            # if qs_key == "status":
            #     where_clause = f"WHERE a.status = '{qs_value}'"
            if query.get("_sortBy"):
                if query['_sortBy'][0] == 'status':
                    sort_by = " ORDER BY a.status"
                if query['_sortBy'][0] == 'location':
                    sort_by = " ORDER BY location_id"
                if query['_sortBy'][0] == 'customer':
                    sort_by = " ORDER BY customer_id"
                if query['_sortBy'][0] == 'name':
                    sort_by = " ORDER BY a.name"
            if query.get("locationId"):
                where_clause = f"WHERE l.id = '{query['locationId'][0]}'"
            if query.get("status"):
                where_clause = f"WHERE a.status = '{query['status'][0]}'"
        # Write the SQL query to get the information you want
        sql_to_execute = f"""
            SELECT
                a.id,
                a.name,
                a.breed,
                a.status,
                a.location_id,
                a.customer_id,
                l.name location_name,
                l.address location_address,
                c.name customer_name,
                c.address customer_address
            FROM Animal a
            JOIN Location l
                ON l.id = a.location_id
            JOIN Customer c
                ON c.id = a.customer_id
            {sort_by}
            {where_clause}
            """
        db_cursor.execute(sql_to_execute)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database

        # Create an animal instance from the current row.
        # Note that the database fields are specified in
        # exact order of the parameters defined in the
        # Animal class above.
        for row in dataset:

            # Create an animal instance from the current row
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])

            # Create a Location instance from the current row
            location = Location(
                row['location_id'], row['location_name'], row['location_address'])

            # Add the dictionary representation of the location to the animal
            animal.location = location.__dict__

            customer = Customer(
                row['customer_id'], row['customer_name'])
            animal.customer = customer.__dict__
            # Add the dictionary representation of the animal to the list
            animals.append(animal.__dict__)

    return animals

# Function with a single parameter


def get_single_animal(id):
    """function for requesting single animal"""
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal
            requested_animal["location"] = get_single_location(
                animal["locationId"])
            requested_animal["customer"] = get_single_customer(
                animal["customerId"])
            requested_animal.pop("locationId", None)
            requested_animal.pop("customerId", None)
    return requested_animal


def create_animal(animal):
    """function for creating an animal"""
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    """function for deleting an animal"""
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)


def update_animal(id, new_animal):
    """function for updating animals"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break
