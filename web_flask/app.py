from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    # Correct the key and the URI spelling
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eatsexpress.sqlite'
    app.config['SECRET_KEY'] = 'your_secret_key'


    db.init_app(app)

    # Import routes after initializing app and db
    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    return app
