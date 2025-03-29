from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
from langchain_community.llms import Bedrock


load_dotenv()


llm = Bedrock(
    credentials_profile_name="isengard", model_id="claude-3-5-sonnet-20240620"
)


async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
