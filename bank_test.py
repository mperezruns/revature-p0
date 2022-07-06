from flask import Flask

bank = Flask(__name__)

@bank.route('/')
def homepage():
    return 'Welcome to Wells Fargo'

@bank.route('/login')
def login():
    return 'Login Page'

if __name__ == "__main__":
    bank.run(host='0.0.0.0', port='8080',debug=True)