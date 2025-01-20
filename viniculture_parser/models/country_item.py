from viniculture_parser.utils import table as table_utils
from viniculture_parser.models import db

class CountryItem(db.instance.Model):
    id = db.instance.Column(db.instance.Integer, primary_key=True)
    name = db.instance.Column(db.instance.String(255), nullable=False)
    quantity = db.instance.Column(db.instance.String(255))
    value = db.instance.Column(db.instance.String(255))
    country_category_id = db.instance.Column(db.instance.Integer, db.instance.ForeignKey("country_category.id"))
    
    @property
    def serialize(self):
        return {
            'name': self.name, 
            'quantity': table_utils.get_database_int(self.quantity),
            'quantity_text': self.quantity,
            'value': table_utils.get_database_int(self.value),
            'value_text': self.value
        }
