from viniculture_parser import config

def get_processing_suboption(request_suboption: str) -> tuple[bool, str]:
    """Retrieves the site processing suboption based on the information provided on the API request.
    
    Args:
      request_suboption: The API requested suboption.
        
    Returns:
      A tuple containing a boolean indicating if the suboption was found and the found suboption value.
    """
    if request_suboption not in config.processing_suboptions_dict:
        return False, ""
    
    return True, config.processing_suboptions_dict[request_suboption]

def get_imported_suboption(request_suboption: str) -> tuple[bool, str]:
    """Retrieves the site imported suboption based on the information provided on the API request.
    
    Args:
      request_suboption: The API requested suboption.
        
    Returns:
      A tuple containing a boolean indicating if the suboption was found and the found suboption value.
    """
    if request_suboption not in config.imported_suboptions_dict:
        return False, ""
    
    return True, config.imported_suboptions_dict[request_suboption]

def get_exported_suboption(request_suboption: str) -> tuple[bool, str]:
    """Retrieves the site exported suboption based on the information provided on the API request.
    
    Args:
      request_suboption: The API requested suboption.
        
    Returns:
      A tuple containing a boolean indicating if the suboption was found and the found suboption value.
    """
    if request_suboption not in config.exported_suboptions_dict:
        return False, ""
    
    return True, config.exported_suboptions_dict[request_suboption]

