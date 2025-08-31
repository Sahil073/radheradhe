from flask import Flask
from flask_cors import CORS
from config import Config

# Initialize app
app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Import routes
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from routes.household_routes import household_bp
from routes.energy_routes import energy_bp
from routes.scenario_routes import scenario_bp

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(household_bp, url_prefix="/api/household")
app.register_blueprint(energy_bp, url_prefix="/api/energy")
app.register_blueprint(scenario_bp, url_prefix="/api/scenario")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
