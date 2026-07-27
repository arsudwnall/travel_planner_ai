from agents import function_tool
from config import logger

@function_tool
def get_currency(destination: str) -> str:
    """
    Returns the local currency for a destination.
    """
    logger.info(f"Getting currency for {destination}")
    currencies = {
        "Japan": "Japanese Yen (JPY)",
        "Paris": "Euro (EUR)",
        "London": "British Pound (GBP)",
        "Goa": "Indian Rupee (INR)"
    }
    return currencies.get(destination, "Unknown")