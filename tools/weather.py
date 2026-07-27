from agents import function_tool
from config import logger

@function_tool
def get_weather(destination: str) -> str:
    """
    Returns the weather for a destination.
    """
    logger.info(f"Getting weather for {destination}")

    weather = {
        "Japan": "Sunny, 26°C",
        "Paris": "Cloudy, 18°C",
        "Goa": "Humid, 32°C",
        "London": "Rainy, 15°C",
        "Bangalore": "Cloudy, 22°C"
    }
    return weather.get(destination, "Weather data unavailable.")