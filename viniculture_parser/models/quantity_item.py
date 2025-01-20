from viniculture_parser.utils import table as table_utils
from viniculture_parser.models.db import db

class QuantityItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.String(255))
    quantity_category_id = db.Column(db.Integer, db.ForeignKey("quantity_category.id"))
    subitems = db.relationship("QuantitySubItem", cascade="all,delete", backref="item")
    
    @property
    def serialize(self):
        return {
            'name': self.name, 
            'quantity': table_utils.get_database_int(self.quantity),
            'quantity_text': self.quantity,
            'items': [i.serialize for i in self.subitems]
        }
