import asyncio   # asynchronous
from dotenv import load_dotenv
from models.response import TripResponse

load_dotenv()   # reads .env and loads OPENAI_API_KEY into the environment

from agents import Runner
from travel_agents.planner import planner_agent

async def main():
    result = await Runner.run(
        planner_agent,
        "Plan a 3 day trip to Japan."
    )
    #print(result.final_output)
    plan: TripResponse = result.final_output
    print(plan.model_dump_json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())