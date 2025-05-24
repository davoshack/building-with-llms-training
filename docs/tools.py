import llm
import os

API_KEY = os.getenv("OPENAI_API_KEY")
model = llm.get_model("gpt-4.1-mini")

def lookup_population(country: str) -> int:
    "Returns the current population of the specified fictional country"
    return 123124

def can_have_dragons(population: int) -> bool:
    "Returns True if the specified population can have dragons, False otherwise"
    return population > 10000

chain_response = model.chain(
    "Can the country of Crumpet have dragons? Answer with only YES or NO",
    tools=[lookup_population, can_have_dragons],
    stream=False,
    key=API_KEY,
)
print(chain_response.text())