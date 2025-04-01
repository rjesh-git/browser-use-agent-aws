from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
import asyncio
from langchain_aws import ChatBedrock


llm = ChatBedrock(
    model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
)


async def main():
    agent = Agent(
        task="""
        1. Find all volleyball events in San Francisco.
        2. Events may be of the following types:
            - Boot camp
            - Workshop
            - Tryout trainings
        3. Find events suitable for age group 11 to 15.
        4. All event should be in 15 miles radius.
        5. Provide me the list of events with details like event name, date, time, location, contact details and age group.
        6. Format result in a table.
        """,
        browser=Browser(config=BrowserConfig(headless=True)),
        llm=llm,
    )
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
