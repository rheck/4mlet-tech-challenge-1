from viniculture_parser.utils import table as table_utils
from viniculture_parser.models.db import db

class CountryCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.String(255))
    value = db.Column(db.String(255))
    year = db.Column(db.String(4), nullable=False)
    modified_date = db.Column(db.String(255))
    items = db.relationship("CountryItem", cascade="all,delete", backref="category")
    
    @property
    def serialize(self):
        return {
            'entity': self.entity,
            'category': self.category,
            'quantity': table_utils.get_database_int(self.quantity),
            'quantity_text': self.quantity,
            'value': table_utils.get_database_int(self.value),
            'value_text': self.value,
            'year': self.year,
            'modified_date': self.modified_date,
            'items': self.items
        }
