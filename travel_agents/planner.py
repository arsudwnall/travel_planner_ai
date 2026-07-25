from agents import Agent

planner_agent = Agent(
    name="Travel Planner",   # identity
    model="gpt-5.4-nano",     # which OpenAI model this agent uses
    instructions="""
    You are an expert travel planner.
    Help users create realistic travel itineraries.
    Always consider:
    - Budget
    - Duration
    - Attractions
    - Practical advice

    Answer in short concise way. 
    """
)