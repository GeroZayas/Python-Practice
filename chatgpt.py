import os
import time
from rich import print
import pyperclip
from markdown import markdown

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# ----------------------------------------------------------------

import openai

openai.api_key = OPENAI_API_KEY

# TODO improve the flow, do not ask for press ENTER to continue
# TODO save interaction to md file


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
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
    prompt = input(
        """
                   (type 'qq' to quit) 
                   --- --- --- --- ---
                   Insert prompt:
                   
                   >>> """
    )

    if prompt == "qq":
        print()
        break

    wait_string = "answer is coming...\n"
    for letter in wait_string:
        print(f"[bold red]{letter}[/bold red]", end="")
        time.sleep(0.05)

    response = generate_response(prompt)

    prompt_and_response = str(f"PROMPT:\n{prompt}\n\nANSWER:\n{response}")

    # copy response to clipboard
    pyperclip.copy(prompt_and_response)

    print("-" * 60)  # separator

    print(f"[bold yellow]{response}[/bold yellow]")

    print("[bold blue]Copied to clipboard![bold blue]")

    print("-" * 60)  # separator

bye_string = "\nThis program is finished now. Have a great day"

for word in bye_string.split():
    print()
    print("          " + word)
    time.sleep(0.2)

time.sleep(1)
