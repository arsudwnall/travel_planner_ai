from agents import Agent
from config import logger
from models.response import TripResponse

logger.info("Initializing Hotel Specialist agent")

hotel_agent = Agent(
    name="Hotel Specialist",
    instructions="""
    You are an expert in hotel recommendations.
    Recommend hotels based on:
    - Budget
    - Travel style
    - Trip duration
    Explain why the hotel is suitable.
    """,
    output_type=TripResponse,
)