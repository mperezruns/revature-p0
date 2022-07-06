from flask import Blueprint, request
from exception.customer_not_found import CustomerNotFoundError
from service.customer_service import CustomerService

cc = Blueprint('customer_controller', __name__)     #Blueprint object
# customer_dao = CustomerService()

# Get all customers (READ)
# Get user by id (READ)
# Add users (CREATE)
# Delete user by id (DELETE)
# Update user by id (UPDATE)

customer_service = CustomerService()

@cc.route('/customers') # GET /Customers
def get_all_customers():
     return {
         "customers": customer_service.get_all_customers()   # a list of dictionaries
     }
    #return {
        #"customers": list(map(lambda e: e.to_dict(), customer_dao.get_all_customers())) # This method returns a list of dictionaries containing each
        # the map function will iterate through our list of Customer objects and individually transform each element
        # in this case, we are transforming each element into a dictionary using our custom to_dict() method
        # inside of the Customer class
        # We are converting into a list
    #}

# @cc.route('/customers/<customer_id', methods=["GET"])    # GET /customers/<customer_id>
# def get_customer_by_id(customer_id):
#     if request.method == "GET":
#         try:
#             return customer_service.get_customer_by_id(customer_id) # dictionary
#         except CustomerNotFoundError as e:
#             return {"message": str(e)
#         }, 404



# @cc.route('/customers/,<customername>')
# def get_customer_by_firstname(customername):
    # pass
    #return customer_dao.get_user_by_customername(customername).to_dict() # This method returns a dictionary containing a single
    # user's information

# @cc.route('/customers', methods=['POST'])
# def add_customer():
    # pass
    #customer_json_dictionary = request.get_json()
    #customer_object = Customer(customer_json_dictionary['customername'], customer_json_dictionary['customer_phone'])
    #return customer_dao.add_customer(customer_object)


# @cc.route('/customers/<customername>', methods=['PUT'])
# def edit_customer_by_customername(customername):
    # pass
    #customer_json_dictionary = request.get_json()
    #customer_object = Customer(customer_json_dictionary['customername'], customer_json_dictionary['customer_phone'])
    #return customer_dao.edit_user_by_customername(customername, customer_object)

