from browser_use import Agent
import asyncio
from dotenv import load_dotenv
from langchain_aws import ChatBedrock


load_dotenv()


llm = ChatBedrock(
    model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
)


async def main():
    agent = Agent(
        task="""
        1. Find me cheapeast flight from San Francisco to Chennai with shortest duration for my vacation.
        2. I want to travel in last week of May and return in June 3rd week, any day is fine.
        3. Economy or Economy plus is fine.
        4. Use google.com/flights to find the flight.
        5. Provide me the top 3 flights with the details like price, duration, and departure time.
        6. Format result in a table with columns: Flight, Price, Duration, Departure Time, Return date.
        7. Provide me the source link to book the flight.
        """,
        llm=llm,
    )
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
