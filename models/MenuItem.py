import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class MenuItem(BaseModel, Base):
    """ Representation of a MenuItem """
    if models.storage_t == 'db':
        __tablename__ = 'menu_items'
        name = Column(String(128), nullable=False)
        price = Column(Integer, nullable=False)
        description = Column(String(256), nullable=True)
        restaurant_id = Column(String(60), ForeignKey('restaurants.id'), nullable=False)
        quantity = Column(Integer, default=0, nullable=False)  # New quantity column
        image = Column(String)


    else:
        name = ""
        price = 0
        description = ""
        restaurant_id = ""
        quantity = 0  # Default quantity for non-db storage
        image = ""

    def __init__(self, *args, **kwargs):
        """ Initializes the menu item """
        super().__init__(*args, **kwargs)
