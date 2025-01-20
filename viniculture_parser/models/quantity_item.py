from viniculture_parser.utils import table as table_utils
from viniculture_parser.models import db

class QuantityItem(db.instance.Model):
    id = db.instance.Column(db.instance.Integer, primary_key=True)
    name = db.instance.Column(db.instance.String(255), nullable=False)
    quantity = db.instance.Column(db.instance.String(255))
    quantity_category_id = db.instance.Column(db.instance.Integer, db.instance.ForeignKey("quantity_category.id"))
    subitems = db.instance.relationship("QuantitySubItem", cascade="all,delete", backref="item")
    
    @property
    def serialize(self):
        return {
            'name': self.name, 
            'quantity': table_utils.get_database_int(self.quantity),
            'quantity_text': self.quantity,
            'items': [i.serialize for i in self.subitems]
        }
