from viniculture_parser import config

def validate_year(year: str) -> tuple[bool, str]:
    """Validates the given year string against the configured minimum and maximum year values.

    Args:
      year: The year string to validate.

    Returns:
      A tuple containing a boolean indicating if the year is valid and an error message if not valid.
    """
    if not year.isdigit():
        return False, "Provided year value is valid number"
    
    year_int = int(year)
    if year_int < config.site_minimun_year or year_int > config.site_maximum_year:
        return False, "The year range should be between {0} and {1}".format(config.site_minimun_year, config.site_maximum_year)
    
    return True, ""