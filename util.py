from fake_useragent import UserAgent


def get_user_agent():
    return UserAgent().random


def replace_space_city(city: str):
    return city.replace(" ", "-") if " " in city else city


def put_city(city: str) -> str:
    return f"{city}-city".strip() if "city" not in city else city
