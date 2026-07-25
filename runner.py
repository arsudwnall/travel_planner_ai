import asyncio   # asynchronous
from dotenv import load_dotenv

load_dotenv()   # reads .env and loads OPENAI_API_KEY into the environment

from agents import Runner
from travel_agents.planner import planner_agent

async def main():
    result = await Runner.run(
        planner_agent,
        "Plan a 5 day trip to Japan."
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())