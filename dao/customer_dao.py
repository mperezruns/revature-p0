from model.customer import Customer
import psycopg

# customers = {
#     "Perez, Mark": {
#         "customername": "Mark Perez",
#         "customer_phone": "626-833-4002"
#     },
#     "Ruelas, Trinity": {
#             "customername": "Trinity Ruelas",
#             "customer_phone": "626-878-8888"
#     }
# }

class CustomerDao:
    # CRUD operations
    # Create -- insert a new user into my "database"
    # Read -- Retrieve a user or users into my "database"
    # Update -- Update a user in my "database"
    # Delete -- Delete a user in my "database"

    def get_all_customers(self):
        # Step 1: open a connection object
        # The "with" keyword will allow us to automatically close the connection object whenever we are done executing
        # the block of code established using the with keyword
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres",
                             password="@zul@6") as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")

            my_list_of_customer_objs = []
            # this will iterate over each row of the users table
            for customers in cur:
                c_id = customers[0]
                first_name = customers[1]
                customer_phone = customers[3]
                active_user = customers[5]

            return my_list_of_customer_objs


# def get_customer_by_id(self, customer_id):
#         with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres",
#                              password="@zul@6") as conn:
#             Automatically close the cursor
            # with conn.cursor() as cur:
            #     cur.execute("INSERT FROM users WHERE id = %s", (customer_id,))
            #cur.fetchone() <--- Tuple ## will delete
            #customer_record = cur.fetchone()   # <---- Tuple
            #return Customer(customer_record[0], customer_record[1], customer_record[2])    # Need to follow the syntax

# def add_customer(self, customer_object):
# first_name_to_add = customer_object.first_name
# last_name_to_add  =
# with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj0", user="postgres",
#                              password="@zul@6") as conn:

    #
    # def edit_customer_by_customername(self, customername, new_customer_info):
    #     if customername == new_customer_info['username']:  # IF we are not updating the customername, replace the rest of the info
    #         customers[customername] = new_customer_info
    #     else:   # Otherwise, delete the original key-value pair and create new key-value pair
    #         del customers[customername]
    #         customers[new_customer_info['customername']] = new_customer_info
    #
    #     return new_customer_info