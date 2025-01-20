from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify
from viniculture_parser.parsers import quantity_parser
from viniculture_parser.utils import validators, mappings
from viniculture_parser.services import quantity as quantity_service
from viniculture_parser.utils.date import get_datetime
from viniculture_parser import config
import traceback

processing = Blueprint("processing", __name__)

@processing.route("/", methods=["GET"])
@jwt_required()
def route():
    site_suboption = request.args.get("category", config.processing_default_suboption)
    is_valid_suboption, suboption = mappings.get_processing_suboption(site_suboption)
    if not is_valid_suboption:
        return jsonify({"success": False, "error": "Category is not valid"})
        
    year = request.args.get("year", "2023")
    is_valid_year, year_validation_error = validators.validate_year(year)
    if not is_valid_year:
        return jsonify({"success": False, "error": year_validation_error})   

    try:
        real_time = True
        parse_date = get_datetime()
        
        parsed_content, totals, totals_text = quantity_parser.parse(config.site_processing_option, suboption, year)
        
        quantity_service.persist_parsed_content(parsed_content, totals_text, site_suboption, year, "processing")
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    
        try:
            real_time = False
            success, parsed_content, totals, totals_text, parse_date = quantity_service.load_parsed_content(site_suboption, year, "processing")

            if success is False:
                raise Exception("Could not find the information in the database.")
        except Exception as i:
            print(i)
            print(traceback.format_exc())
            
            return jsonify({"success": False, "error": "Could not connect to the source site or the database."})
            
    
    return jsonify({
        "success": True,
        "year": year,
        "category": site_suboption,
        "totals": totals,
        "totals_text": totals_text,
        "data": parsed_content,
        "is_realtime": real_time,
        "parse_date": parse_date
    }), 201
