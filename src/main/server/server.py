from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

# importar blueprints
from src.main.routes.album_routes import album_route_bp
from src.main.routes.photo_routes import photo_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(album_route_bp)
app.register_blueprint(photo_route_bp)

