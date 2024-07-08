from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Importing routes from different modules
from routes.main import *
from routes.auth import *
from routes.account import *
from routes.admin import *
from routes.cart import *
from routes.orders import *
from routes.restaurants import *

if __name__ == "__main__":
    app.run(debug=True)
