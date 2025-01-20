def get_column_int(column):
    """Extracts the value from a table column.
    
    Args:
      column: The column to extract the value from.
      
    Returns:
      The column value as an integer.
    """
    quantity_text = column.text.strip()
    
    if quantity_text == '-':    
        return 0

    return int(quantity_text.replace(".", ""))

def get_database_int(column):
    """Extracts the value from the database column.
    
    Args:
      column: The database column to extract the value from.
      
    Returns:
      The database column value as an integer.
    """
    if column == '-':    
          return 0

    return int(column.replace(".", ""))
