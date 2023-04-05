EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

def get_all_employees():
    """function for viewing all employees"""
    return EMPLOYEES


def get_single_employee(id):
    """function for getting individual employee by id"""
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee
