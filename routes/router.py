from flask import Blueprint
from routes.area_forecast_router import area_forecast_router_bp

router_bp = Blueprint("router_bp", __name__, url_prefix="/api")

router_bp.register_blueprint(area_forecast_router_bp)
