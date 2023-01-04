from util import get_user_agent, put_city, replace_space_city
from selectolax.parser import HTMLParser
import httpx
from typing import Dict


class WeatherApp:
    def __init__(self, city: str):
        self.city: str = city
        self.weather_source: str = "https://www.wunderground.com/weather/ph/"
        self.headers: Dict = {
            "User-Agent": get_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "Accept-Encoding": "none",
            "Accept-Language": "en-US,en;q=0.8",
            "Connection": "keep-alive",
        }

    def get_city_weather(self):

        # TODO: extract and clean city
        city = put_city(self.city)
        city = replace_space_city(city).lower()

        # TODO: get html from web
        html: HTMLParser = self.get_weather(city)

        # TODO: parse the html
        weather_info: tuple = self.get_weather_info(html)

        # TODO: display the forcast
        self.print_weather(weather_info)

    def get_html(self, url: str) -> HTMLParser:
        return HTMLParser(httpx.get(url, headers=self.headers).text)

    def get_weather_info(self, html: HTMLParser) -> tuple:
        temperature: int = int(html.css_first("span.wu-value").text())
        weather: str = html.css_first("div.condition-icon p").text()
        temperature_sign: str = html.css_first("span.wu-label").text()
        return (weather, temperature, temperature_sign)

    def get_weather(self, city: str):
        url: str = f"{self.weather_source}{city}"
        return self.get_html(url)


    def print_weather(self, weather_info: tuple) -> None:
        weather, temperature, temperature_sign = weather_info
        print(f"Today is {weather} and {temperature}{temperature_sign} in {city}")


def print_header():
    print("-" * 15)
    print("  WEATHER APP")
    print("-" * 15)

if __name__ == "__main__":
    print_header()
    city: str = input("Enter City: ")
    city_weather = WeatherApp(city)
    city_weather.get_city_weather()
