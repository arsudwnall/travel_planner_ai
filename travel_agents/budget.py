from agents import Agent
from config import logger
from models.response import TripResponse

logger.info("Initializing Budget Analyst agent")

budget_agent = Agent(
    name="Budget Analyst",
    instructions="""
    You are an expert in travel budgeting.
    Analyze the user's budget against estimated costs for
    hotel, food, transport and activities.
    Flag if the trip is over budget and suggest adjustments.
    """,
    output_type=TripResponse,
)