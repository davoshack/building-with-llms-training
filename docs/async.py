import asyncio
import llm

model = llm.get_async_model("gpt-4.1-mini")
async def main():
    response = model.prompt(
        "A joke about a walrus who lost his shoes"
    )
    async for chunk in response:
        print(chunk, end="", flush=True)

asyncio.run(main())