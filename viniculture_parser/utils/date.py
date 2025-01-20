from viniculture_parser import config
from datetime import datetime
import pytz

def get_datetime() -> str:
    """Util function to return the actual datetime, considering the configured timezone.
    
    Returns:
        A formated string of the actual datetime.
    """
    timezone_str = config.application_timezone    
    timezone = pytz.timezone(timezone_str)
    
    return datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
