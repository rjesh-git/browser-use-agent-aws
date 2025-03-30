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
        task="Get the 2025 holiday schedule for LAUSD.",
        llm=llm,
    )
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
