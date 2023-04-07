import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal, get_single_location, get_all_locations
from views import get_single_customer, get_all_customers, get_all_employees, get_single_employee
from views import create_animal, create_location, create_employee, create_customer, delete_animal
from views import delete_employee, delete_customer, delete_location, update_animal, update_employee, update_customer, update_location
# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.


class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Here's a class function

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        # self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)
        if resource == "animals":
            if id is not None:
                response = get_single_animal(id)
            else:
                response = get_all_animals()
            if response is None:
                self._set_headers(404)
                response = {"message": f"Animal {id} is not found"}
            else:
                self._set_headers(200)
        if resource == "locations":
            if id is not None:
                response = get_single_location(id)
            else:
                response = get_all_locations()
            if response is None:
                self._set_headers(404)
                response = {"message": f"Location {id} is not found"}
            else:
                self._set_headers(200)
        if resource == "customers":
            if id is not None:
                response = get_single_customer(id)
            else:
                response = get_all_customers()
            if response is None:
                self._set_headers(404)
                response = {"message": f"Customer {id} is not found"}
            else:
                self._set_headers(200)
        if resource == "employees":
            if id is not None:
                response = get_single_employee(id)
            else:
                response = get_all_employees()
            if response is None:
                self._set_headers(404)
                response = {"message": f"Employee {id} is not found"}
            else:
                self._set_headers(200)
        # if response is not None:
        #     self._set_headers(200)
        self.wfile.write(json.dumps(response).encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.

    #  OLD POST FORMAT
    # def do_POST(self):
    #     """Handles POST requests to the server"""

    #     # Set response code to 'Created'
    #     self._set_headers(201)

    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)
    #     response = {"payload": post_body}
    #     self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """function for posting new dictionaries"""
        # self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        # print(post_body) PRINTS b'{\n    "id": 1,\n    "name": "rover",\n    "species": "Dog",\n    "status": "Admitted",\n    "locationId": 1,\n    "customerId": 1\n}'
        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)
        response = {}
        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_animal = None
        new_location = None
        new_employee = None
        new_customer = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "animals":
            if "name" in post_body and "species" in post_body and "status" in post_body and "customerId" in post_body and "locationId" in post_body:
                new_animal = create_animal(post_body)
                response = new_animal
                self._set_headers(201)
            else:
                self._set_headers(400)
                response = {
                    "message": f'{"name is required" if "name" not in post_body else ""} {"status is required" if "status" not in post_body else ""} {"customerId is required" if "customerId" not in post_body else ""} {"locationId is required" if "locationId" not in post_body else ""} {"species is required" if "species" not in post_body else ""}'
                }
        # Encode the new animal and send in response
        if resource == "locations":
            if "name" in post_body and "address" in post_body:
                new_location = create_location(post_body)
                response = new_location
                self._set_headers(201)
            else:
                self._set_headers(400)
                response = {
                    "message": f'{"name is required" if "name" not in post_body else ""} {"address is required" if "address" not in post_body else ""}'}
        if resource == "employees":
            if "name" in post_body:
                new_employee = create_employee(post_body)
                response = new_employee
                self._set_headers(201)
            else:
                self._set_headers(400)
                response = {
                    "message": "name is required"
                }
        if resource == "customers":
            if "name" in post_body:
                new_customer = create_customer(post_body)
                response = new_customer
                self._set_headers(201)
            else:
                self._set_headers(400)
                response = {
                    "message": "name is required"
                }
        self.wfile.write(json.dumps(response).encode())

    # A method that handles any PUT request.

    def do_PUT(self):
        """Handles PUT requests to the server"""
        # self.do_PUT()
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        if resource == "animals":
            update_animal(id, post_body)
            self.wfile.write("".encode())
        if resource == "locations":
            update_location(id, post_body)
            self.wfile.write("".encode())
        if resource == "customers":
            update_customer(id, post_body)
            self.wfile.write("".encode())
        if resource == "employees":
            update_employee(id, post_body)
            self.wfile.write("".encode())

    def do_DELETE(self):
        """function for removing animal from database"""
        # Set a 204 response code
        # self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            self._set_headers(204)
            delete_animal(id)
        # Encode the new animal and send in response
            self.wfile.write("".encode())
        if resource == "locations":
            delete_location(id)
            self._set_headers(204)
            self.wfile.write("".encode())
        if resource == "customers":
            # delete_customer(id)
            self._set_headers(405)
            response = {"message": "Deleting customers requires contacting the company directly"}
            self.wfile.write(json.dumps(response).encode())
        if resource == "employees":
            delete_employee(id)
            self._set_headers(204)
            self.wfile.write("".encode())
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def parse_url(self, path):
        """turns url for requested animal into tuple"""
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
