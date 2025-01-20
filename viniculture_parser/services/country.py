from viniculture_parser.models import country_category, country_item
from viniculture_parser.models.db import db
from viniculture_parser.utils.date import get_datetime
from viniculture_parser.utils.table import get_database_int

def persist_parsed_content(parsed_content, quantity, value, category, year, entity):
    already_exists = country_category.CountryCategory.query.filter_by(category=category, year=year, entity=entity).first()
    if already_exists is not None:
        db.session.delete(already_exists)
        db.session.commit()
    
    new_category = country_category.CountryCategory(
        entity=entity,
        category=category,
        quantity=quantity,
        value=value,
        year=year,
        modified_date=get_datetime())
    
    for item in parsed_content:
        new_item = country_item.CountryItem(
            name=item["name"],
            quantity=item["quantity_text"],
            value=item["value_text"])
        
        new_category.items.append(new_item)
    
    db.session.add(new_category)
    db.session.commit()

def load_parsed_content(category, year, entity) -> tuple[bool, list, int, str, int, str, str]:
    saved_category = country_category.CountryCategory.query.filter_by(category=category, year=year, entity=entity).first()
    if saved_category is None:
        return (False, [], 0, "", 0, "", "")
    
    return True, [i.serialize for i in saved_category.items], get_database_int(saved_category.quantity), saved_category.quantity, get_database_int(saved_category.value), saved_category.value, saved_category.modified_date
