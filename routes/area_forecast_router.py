from flask import Blueprint
from controllers.area_forecast_controller import AreaForecastController

area_forecast_router_bp = Blueprint(
    "area_forecast_router_bp", __name__, url_prefix="/forecast")


@area_forecast_router_bp.route("/", methods=["POST"])
def find_area_forecast():
    return AreaForecastController.find_area_forecast()
