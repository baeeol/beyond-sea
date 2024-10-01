from api.api import Openweather
from utils.utils import Time
from typing import TypedDict


class Forecast(TypedDict):
    date: str
    weather: str
    temperature: str
    wind_chill: str
    humidity: str


class AreaForecastService:
    @staticmethod
    def find_area_forecast(area_name: str) -> list[Forecast]:
        # 지역의 3시간 단위의 하루치 기상예보 데이터 얻기
        forecast_data = Openweather.get_days_forecast_every_3hour(area_name)

        # 기상예보 데이터 필터링 및 예보 시각을 현지 시각으로 변경
        forecast: list = []
        for forecast_data_on_hour in forecast_data['list']:
            # 데이터 필터링
            weather_code = forecast_data_on_hour['weather'][0]['main']
            weather = {"Clear": "맑음", "Clouds": "흐림",
                       "Rain": "비"}[weather_code]
            temperature = round(forecast_data_on_hour['main']['temp'])
            wind_chill = round(forecast_data_on_hour['main']['feels_like'])
            humidity = forecast_data_on_hour['main']['humidity']

            # 기상예보 날짜를 UTC에서 현지 날짜로 변경
            local_forecast_date = Time.get_date_by_unix_time(
                forecast_data_on_hour['dt'] + forecast_data['city']['timezone'])
            month = local_forecast_date['month']
            day = local_forecast_date['day']
            hour = Time.convert_24hour_to_12hour(local_forecast_date['hour'])

            forecast.append({
                "date": f"{month}월 {day}일 ({hour}시)",
                "weather": weather,
                "temperature": f"{temperature}°C",
                "wind_chill": f"{wind_chill}°C",
                "humidity": f"{humidity}%",
            })

        return forecast
