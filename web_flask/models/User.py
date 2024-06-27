from hashlib import md5
from main import db  # Assuming 'db' is your SQLAlchemy instance

class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(256), nullable=True)
    orders = db.relationship("Order", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'User with name {self.first_name} and email {self.email}'

    def __setattr__(self, name, value):
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
