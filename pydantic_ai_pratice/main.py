from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
import os
from dotenv import load_dotenv
from rich import print
from datetime import datetime

from utils import scraper, random_name

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

now = datetime.now().strftime("%Y_%M_%d-%H_%M_%S")
print(f"{now= }")

s = input("hit enter to continue")

provider = GoogleProvider(api_key=GOOGLE_API_KEY)
model = GoogleModel("gemini-2.5-flash", provider=provider)

advice_agent = Agent(
    model,
    deps_type=str,
    system_prompt=(
        "You provide the best programming advice based  on the user's problem."
        "You give it a bit of programming humor, too"
    ),
)


summary_agent = Agent(
    model,
    deps_type=str,
    system_prompt=(
        "You provide a summary of the input text with a bit of humor."
        "If you are asked for a random name, provide it, and give a crazy explanation of what the name means"
    ),
)


summary_agent.tool_plain(scraper)
summary_agent.tool_plain(random_name)

user_input = input("Talk to the agent:\n>>> ")

deps = "The user lives in Barcelona"

# res = advice_agent.run_sync(user_input, deps=deps)
res = summary_agent.run_sync(user_input)
print(res.output)

clean_user_input = (
    user_input.strip()
    .lower()
    .replace(" ", "_")
    .replace(",", "_")
    .replace("/", "")
    .replace(".", "_")[:30]
)

print(f"{clean_user_input= }")

response_name = f"{clean_user_input}_{now}"
try:
    with open(f"./responses/{response_name}.md", "w") as f:
        f.write(res.output)
except Exception as e:
    print("A problem has ocurred while trying to save the file:", e)
