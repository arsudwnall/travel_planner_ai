from agents import Agent
from config import logger
from models.response import TripResponse

logger.info("Initializing Itinerary Builder agent")

itinerary_agent = Agent(
    name="Itinerary Builder",
    instructions="""
    You are an expert in building day-by-day travel itineraries.
    Combine weather, hotel and budget information into a clear,
    day-wise plan.
    """,
    output_type=TripResponse,
)