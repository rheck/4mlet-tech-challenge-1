from viniculture_parser.utils import table as table_utils
from viniculture_parser.models import db

class QuantityCategory(db.instance.Model):
    id = db.instance.Column(db.instance.Integer, primary_key=True)
    entity = db.instance.Column(db.instance.String(255), nullable=False)
    category = db.instance.Column(db.instance.String(255), nullable=False)
    quantity = db.instance.Column(db.instance.String(255))
    year = db.instance.Column(db.instance.String(4), nullable=False)
    modified_date = db.instance.Column(db.instance.String(255))
    items = db.instance.relationship("QuantityItem", cascade="all,delete", backref="category")
    
    @property
    def serialize(self):
        return {
            'entity': self.entity,
            'category': self.category,
            'quantity': table_utils.get_database_int(self.quantity),
            'quantity_text': self.quantity,
            'year': self.year,
            'modified_date': self.modified_date,
            'items': self.items
        }
