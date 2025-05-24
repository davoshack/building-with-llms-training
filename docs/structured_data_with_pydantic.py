import llm, json
from pydantic import BaseModel

class Pelican(BaseModel):
    name: str
    age: int
    short_bio: str
    beak_capacity_ml: float

model = llm.get_model("gpt-4o-mini")
response = model.prompt("Describe a spectacular pelican", schema=Pelican)
pelican = json.loads(response.text())
print(json.dumps(pelican, indent=2))