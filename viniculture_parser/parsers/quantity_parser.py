from viniculture_parser.utils import table as table_utils
from viniculture_parser import config
from bs4 import BeautifulSoup
import requests
import os

def parse(site_option, site_suboption, year):
    """Parses the table data from the website based on the given options, suboption, and year.
    This parser reads the text and quantity columns from the table.

    Args:
      site_option: The option to use for parsing.
      site_suboption: The suboption to use for parsing.
      year: The year to parse data for.

    Returns:
      A tuple containing the parsed content, total quantity, total quantity text, total value, and total value text.
    """
    url = '{0}?opcao={1}&ano={2}'.format(config.site_base_url, site_option, year)
    
    if site_suboption is not None:
        url += '&subopcao={0}'.format(site_suboption)
    
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    
    table = soup.find('table', class_='tb_base tb_dados')
    
    category = None
    parsed_content = {}
    
    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        
        if 'tb_item' in columns[0]['class']:
            category = columns[0].text.strip()
            
            parsed_content[category] = {
                'name': category,
                'quantity': table_utils.get_column_int(columns[1]),
                'quantity_text': columns[1].text.strip(),
                'items': []
            }
            continue
            
        parsed_content[category]['items'].append({
            'name': columns[0].text.strip(), 
            'quantity': table_utils.get_column_int(columns[1]),
            'quantity_text': columns[1].text.strip()
        })
    
    total_columns = table.tfoot.find('tr').find_all('td')
        
    return list(parsed_content.values()), table_utils.get_column_int(total_columns[1]), total_columns[1].text.strip()
