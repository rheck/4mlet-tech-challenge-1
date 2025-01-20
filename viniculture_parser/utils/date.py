from viniculture_parser import config
from datetime import datetime
import pytz

def get_datetime() -> str:
    timezone_str = config.application_timezone    
    timezone = pytz.timezone(timezone_str)
    
    return datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
