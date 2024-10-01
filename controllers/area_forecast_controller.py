from services.area_forecast_service import AreaForecastService
from responses.response import Response, ResponseTemplate
from utils.utils import Time
from flask import request


class AreaForecastController:
    @staticmethod
    def find_area_forecast():
        req = request.get_json()
        area_name: str = req['action']['params']['areaName']
        area_forecast = AreaForecastService.find_area_forecast(area_name)

        response_template = ResponseTemplate()
        response_template.add_text_output(f"{area_name}의 예상 날씨입니다.")
        itemcards = []
        for area_forecast_on_hour in area_forecast:
            itemcards.append({
                "title": area_forecast_on_hour['date'],
                "items": [
                    {"title": "날씨",
                        "description": area_forecast_on_hour['weather']},
                    {"title": "온도",
                        "description": area_forecast_on_hour['temperature']},
                    {"title": "체감온도",
                     "description": area_forecast_on_hour['wind_chill']},
                    {"title": "습도",
                     "description": area_forecast_on_hour['humidity']},
                ]
            })
        response_template.add_itemcard_carousel_output(itemcards)

        response = Response()
        response.set_template(response_template)
        return response.jsonify()
