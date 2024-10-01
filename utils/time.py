from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
import time

load_dotenv()

api_key = os.environ.get("OPENWEATHER_API_KEY")


class Date(TypedDict):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    wday: Literal["월", "화", "수", "목", "금", "토", "일"]


class Time:
    @staticmethod
    def get_date_by_unix_time(unix_time: int) -> Date:
        """
        unix 시간으로 날짜를 얻습니다.
        """

        date_obj = time.gmtime(unix_time)

        return {
            "year": date_obj.tm_year,
            "month": date_obj.tm_mon,
            "day": date_obj.tm_mday,
            "hour": date_obj.tm_hour,
            "minute": date_obj.tm_min,
            "second": date_obj.tm_sec,
            "wday": f"{['월', '화', '수', '목', '금', '토', '일'][date_obj.tm_wday]}",
        }

    @staticmethod
    def convert_24hour_to_12hour(hour: int) -> str:
        """
        24시 표기법을 12시 표기법으로 변환합니다.
        """

        if (hour <= 12):
            return f"오전 {hour}"
        else:
            return f"오후 {hour-12}"
