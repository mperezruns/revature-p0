class Customer:
    # Define a __init__ method to customer class
    def __init__(self, id, customername, customer_phone, active_user):
        self.id =id
        self.customername = customername
        self.customer_phone = customer_phone
        self.active_user = active_user

        def to_dict(self):
            return {
                "id": self.id,
                "customername": self.customername,
                "customer_phone": self.customer_phone,
                "active_customer": self.active
            }