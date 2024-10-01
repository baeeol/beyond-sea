from .open_api import OpenAPI
import requests


class Openweather(OpenAPI):
    @staticmethod
    def get_days_forecast_every_3hour(area_name: str) -> None:
        """
        특정 지역의 3시간 단위 하루치 기상예보 데이터를 얻습니다. \n
        기상예보 날짜는 UTC 입니다.
        """

        # 특정 지역의 위도, 경도 얻기
        area_name_and_location = requests.get(
            ("http://api.openweathermap.org/geo/1.0/direct?"
             f"q={area_name}"
             f"&appid={super(Openweather, Openweather).get_env('OPENWEATHER_API_KEY')}")
        ).json()
        latitude = area_name_and_location[0]['lat']
        longitude = area_name_and_location[0]['lon']

        return requests.get(
            ("https://api.openweathermap.org/data/2.5/forecast?"
             f"lat={latitude}&lon={longitude}"
             f"&units=metric&cnt=8"
             f"&appid={super(Openweather, Openweather).get_env('OPENWEATHER_API_KEY')}")
        ).json()
