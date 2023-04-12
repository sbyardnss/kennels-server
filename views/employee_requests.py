import json
import sqlite3
from models import Employee
EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]


def get_all_employees():
    """sql get all employees"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        """)
        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])
            employees.append(employee.__dict__)
    return employees


def get_single_employee(id):
    """sql single employee fetch"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE id = ?
        """, (id, ))
        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'],
                            data['address'], data['location_id'])
    return employee.__dict__


def get_employee_by_location(location):
    """function for querying employee by location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """, ( location, ))
        dataset = db_cursor.fetchall()
        employees = []
        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])
            employees.append(employee.__dict__)
    return employees
# OLD VERSIONS
# def get_all_employees():
#     """function for viewing all employees"""
#     return EMPLOYEES


# def get_single_employee(id):
#     """function for getting individual employee by id"""
#     requested_employee = None

#     for employee in EMPLOYEES:
#         if employee["id"] == id:
#             requested_employee = employee
#     return requested_employee

def create_employee(employee):
    """function for adding an employee to the database"""
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    """function for deleting an employee"""
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """function for updating a employee"""
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
