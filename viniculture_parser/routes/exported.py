from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify
from viniculture_parser.parsers import countries_parser
from viniculture_parser.utils import validators, mappings
from viniculture_parser.services import country as country_service
from viniculture_parser.utils.date import get_datetime
from viniculture_parser import config

exported = Blueprint("exported", __name__)

@exported.route("/", methods=["GET"])
@jwt_required()
def route():
    site_suboption = request.args.get("category", config.exported_default_suboption)
    is_valid_suboption, suboption = mappings.get_exported_suboption(site_suboption)
    if not is_valid_suboption:
        return jsonify({"success": False, "error": "Category is not valid"})
        
    year = request.args.get("year", "2023")
    is_valid_year, year_validation_error = validators.validate_year(year)
    if not is_valid_year:
        return jsonify({"success": False, "error": year_validation_error})   

    try:
        real_time = True
        parse_date = get_datetime()
        parsed_content, totals, totals_text, value, value_text = countries_parser.parse(config.site_exported_option, suboption, year)

        country_service.persist_parsed_content(parsed_content, totals_text, value_text, site_suboption, year, "exported")
    except:
        try:
            real_time = False
            success, parsed_content, totals, totals_text, value, value_text, parse_date = country_service.load_parsed_content(site_suboption, year, "exported")

            if success is False:
                raise Exception("Could not find the information in the database.")
        except:
            return jsonify({"success": False, "error": "Could not connect to the source site or the database."})
    
    return jsonify({
        "success": True,
        "year": year,
        "category": site_suboption,
        "totals": totals,
        "totals_text": totals_text,
        "value": value,
        "value_text": value_text,
        "data": parsed_content,
        'is_realtime': real_time,
        'parse_date': parse_date
    }), 201
