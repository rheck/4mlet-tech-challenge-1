from viniculture_parser.models import quantity_category, quantity_item, quantity_subitem
from viniculture_parser.models.db import db
from viniculture_parser.utils.date import get_datetime
from viniculture_parser.utils.table import get_database_int

def persist_parsed_content(parsed_content, quantity, category, year, entity):
    """Service to persist the parsed content to the database.
    
    Args:
      parsed_content: Array of items scrapped from Embrapa site.
      quantity: Text value of the quantity.
      category: Category of the information.
      year: Data parsed year.
      entity: Information about which section of Embrapa site the information is comming from.
    """
    already_exists = quantity_category.QuantityCategory.query.filter_by(category=category, year=year, entity=entity).first()
    if already_exists is not None:
        db.session.delete(already_exists)
        db.session.commit()
    
    new_category = quantity_category.QuantityCategory(
        entity=entity,
        category=category,
        quantity=quantity,
        year=year,
        modified_date=get_datetime())
    
    for item in parsed_content:
        new_item = quantity_item.QuantityItem(
            name=item["name"],
            quantity=item["quantity_text"])
        
        for subitem in item["items"]:
            new_subitem = quantity_subitem.QuantitySubItem(
                name=subitem["name"],
                quantity=subitem["quantity_text"])
            
            new_item.subitems.append(new_subitem)
        
        new_category.items.append(new_item)
    
    db.session.add(new_category)
    db.session.commit()

def load_parsed_content(category, year, entity) -> tuple[bool, list, int, str, str]:
    """Service to load the persisted data from database.
    
    Args:
      category: Category of the information.
      year: Data parsed year.
      entity: Information about which section of Embrapa site the information is comming from.
      
    Returns:
        A tuple with a boolean flag of success, the list of persisted content, the quantity number, the quantity text, and the modified date.
    """
    saved_category = quantity_category.QuantityCategory.query.filter_by(category=category, year=year, entity=entity).first()
    if saved_category is None:
        return (False, [], 0, "", "")
    
    return True, [i.serialize for i in saved_category.items], get_database_int(saved_category.quantity), saved_category.quantity, saved_category.modified_date
