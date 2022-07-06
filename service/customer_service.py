from dao.customer_dao import CustomerDao

class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDao()

    # Get a customer object from the DAO layer
    # convert the Customer objects into dictionaries
    # return a list of dictionaries that each represent the users
    def get_all_customers(self):
        list_of_customer_objects = self.customer_dao.get_all_customers()


        # Method #1, use a for loop and do it manually
        list_of_customer_dictionaries = []
        for customer_obj in list_of_customer_objects:
             list_of_customer_dictionaries.append(customer_obj.to_dict())

        return list_of_customer_dictionaries

        # Method #2, use map
        # return list(map(lambda x: x.to_dict(), list_of_customer_objects))

    # Get Customer object from DAO and convert into a dictionary
# def get_customer_by_id(self, customer_id):
#     customer_obj = self.user_dao.get_customer_by_id(customer_id)  # user_dao.get_user_by_id will either give us None or a User
#     object
    #
    # if not customer_obj:
    #     raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")


    # def delete_customer_by_id(self, customer_id):
    # customer_by_id = self.customer_dao.delete_customer_by_id(customer_id)
    #
    #if not customer_by_id:
    # raise CustomerNotFoundError

    # Invoke ADD_CUSTOMER IN DAO, passing in a customer_object
    # Return the dictionary representation of the return value from that method
    # def add_customer(self, customer_object):
    #     added_customer_object = self.customer_dao.add_customer(customer_object)
    #     return added_customer_object.to_dict()
    #
    # Invoke edit_customer in DAO, passing in a customer_object
    # Return the dictionary representation of the return value from te customer_by_customername method
    # def edit_customer_by_customername(self, customername, customer_object):
    #     edited_customer_obj = self.customer_dao.edit_by_customername(customername, customer_object)
        # return edited_customer_obj.to_dict()