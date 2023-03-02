import os
import time
from rich import print


from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# ----------------------------------------------------------------

import openai

openai.api_key = OPENAI_API_KEY


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,  # number of responses
        stop=None,
        
        # temperature -> specifies the "creativity" of the language model.
        # A higher temperature value will result
        # in more creative and varied responses, while a lower temperature value will result in more predictable and conservative responses.
        
        temperature=0.5,
    )
    return response.choices[0].text.strip()


print("-" * 60)

# ----------------------------------------------------------------
# MAIN LOOP

program_run = True


print()  # blank line


while program_run:
    prompt = input("Insert prompt: \n>>> ")
    response = generate_response(prompt)

    print("-" * 60)  # separator

    print(f"[bold yellow]{response}[/bold yellow]")

    print("-" * 60)  # separator

    user_quit = input('Hit >>> ENTER to continue or >>> "q" to quit\n\n')

    if user_quit == "q":
        print()
        break

bye_string = "\nThis program is finished now. Have a great day"

for word in bye_string.split():
    print()
    print("          " + word)
    time.sleep(0.2)

time.sleep(1)
