from flask import Flask
from controller.customer_controller import cc   # Here I am importing from the customer_controller.py

app = Flask(__name__)   # Instanciating an app object

# The pupose of this if statement is so that if another file imports this files, then
# the code inside of the if block will not run, since __name__ would not be __main__
# in that situation
if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/')
    @app.route("/home")
    @app.route("/index")
    def home_page():
        return "Welcome to Citi Bank"

    app.register_blueprint(cc)

    # @cc.route('/customers')  # GET /users
    # def get_all_customers():
    #     return {
    #         "customers": customer_service.get_all_customers()  # a list of dictionaries
    #     }


    app.run(port=5000, debug=True)  # Start up the web server on port 8080

