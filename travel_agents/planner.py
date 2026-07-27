from agents import Agent
from config import logger
from models.response import TripResponse
from tools.weather import get_weather
from tools.currency import get_currency
from tools.packing import get_packing_list
from travel_agents.hotel import hotel_agent
from travel_agents.itinerary import itinerary_agent
from travel_agents.budget import budget_agent

logger.info("Initializing Travel Planner agent")

# Planner agent
planner_agent = Agent(
    name="Travel Planner",   # identity
    model="gpt-5.4-nano",     # which OpenAI model this agent uses
    instructions="""
    You are the primary travel planner and orchestrator.
    Coordinate the Hotel Agent, Budget Agent and Itinerary
    Agent to produce one complete, realistic travel plan.
    Check weather and currency first, then delegate hotel and
    budget questions, and finish by building the itinerary.
    Answer in very short concise way.
    """,
    tools=[get_weather, get_currency, get_packing_list],
    handoffs=[hotel_agent, itinerary_agent, budget_agent],
    output_type=TripResponse,
)