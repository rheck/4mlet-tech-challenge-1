from dotenv import load_dotenv
import os

load_dotenv()

debug_application = os.environ.get("DEBUG", False)
application_timezone = os.environ.get("TIMEZONE", "America/Sao_Paulo")

site_base_url = os.getenv("SERVICE_BASE_URL", "")
database_url = os.getenv("DATABASE_URL", "")
jwt_secret_key = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")

site_minimun_year = 1970
site_maximum_year = 2023

site_production_option = "opt_02"
site_processing_option = "opt_03"
site_commercialization_option = "opt_04"
site_imported_option = "opt_05"
site_exported_option = "opt_06"

processing_default_suboption = "viniferas"
processing_suboptions_dict = dict(
    viniferas           = "subopt_01",
    american_and_hybrid = "subopt_02",
    table_grapes        = "subopt_03",
    unclassified        = "subopt_04",
)

imported_default_suboption = "table_grapes"
imported_suboptions_dict = dict(
    table_grapes = "subopt_01",
    sparkling    = "subopt_02",
    fresh_grapes = "subopt_03",
    raisins      = "subopt_04",
    grape_juice  = "subopt_05",
)

exported_default_suboption = "table_grapes"
exported_suboptions_dict = dict(
    table_grapes = "subopt_01",
    sparkling    = "subopt_02",
    fresh_grapes = "subopt_03",
    grape_juice  = "subopt_04"
)
