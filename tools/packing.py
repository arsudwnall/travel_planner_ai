from agents import function_tool
from config import logger

@function_tool
def get_packing_list(destination: str) -> str:
    """
    Returns a suggested packing list for a destination.
    """
    logger.info(f"Getting packing list for {destination}")
    packing_lists = {
        "Japan": "Comfortable walking shoes, light jacket, portable Wi-Fi",
        "Paris": "Umbrella, light sweater, walking shoes",
        "London": "Raincoat, umbrella, layered clothing",
        "Goa": "Sunscreen, light cotton clothes, sandals"
    }
    return packing_lists.get(destination, "Standard travel essentials")