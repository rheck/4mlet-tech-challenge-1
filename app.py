from flask import Flask, jsonify, send_file
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
import io

from viniculture_parser import config
from viniculture_parser.models.db import db
from viniculture_parser.routes.authentication import authentication
from viniculture_parser.routes.production import production
from viniculture_parser.routes.commercialization import commercialization
from viniculture_parser.routes.processing import processing
from viniculture_parser.routes.imported import imported
from viniculture_parser.routes.exported import exported

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = config.jwt_secret_key
app.config["JWT_VERIFY_SUB"] = False

jwt = JWTManager(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(authentication, url_prefix="/authentication")
app.register_blueprint(production, url_prefix="/production")
app.register_blueprint(processing, url_prefix="/processing")
app.register_blueprint(commercialization, url_prefix="/commercialization")
app.register_blueprint(imported, url_prefix="/imported")
app.register_blueprint(exported, url_prefix="/exported")

@app.route("/swagger")
def swagger():
    """Route to read the swagger.yaml file and returns it.
    
    Returns:
        A YAML binary content.
    """
    with open("swagger.yaml", "rb") as f:
        bytes = io.BytesIO(f.read())
    return send_file(bytes, mimetype="application/yaml")

swaggerui_blueprint = get_swaggerui_blueprint(
    "/swagger-ui",
    "/swagger",
    config={"app_name": "Tech Challenge 1 - Viniculture Parser"}
)
app.register_blueprint(swaggerui_blueprint)

if __name__ == "__main__":
    app.run(debug=config.debug_application)
