import os
import time
from datetime import date

import pyperclip
from dotenv import load_dotenv
from markdown import markdown
from rich import print

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# DATE
# ----------------------------------------------------------------
today = date.today()

# OPENAI IMPORT AND INIT
# ----------------------------------------------------------------

import openai

openai.api_key = OPENAI_API_KEY


# FUNCTION DEFINITIONS
# ----------------------------------------------------------------
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

# MAIN LOOP
# ----------------------------------------------------------------
program_run = True

print()  # blank line

while program_run:
    # ASK USER CHOICE
    # ----------------------------------------------------------------
    prompt = input(
        """
                   (type 'qq' to quit) 
                   --- --- --- --- ---
                   Insert prompt:
                   
                   >>> """
    )

    # TERMINATE PROGRAM IF 'qq'
    # ----------------------------------------------------------------
    if prompt == "qq":
        print()
        break

    # LET USER KNOW THE PROGRAM IS RUNNING WELL
    # ----------------------------------------------------------------
    wait_string = "answer is coming...\n"
    for letter in wait_string:
        print(f"[bold red]{letter}[/bold red]", end="")
        time.sleep(0.05)

    response = generate_response(prompt)

    prompt_and_response = str(f"PROMPT:\n{prompt}\n\nANSWER:\n{response}")

    # copy response to clipboard
    pyperclip.copy(prompt_and_response)

    # PRINT RESPONSE
    # ----------------------------------------------------------------

    print("-" * 60)  # separator

    print(f"[bold yellow]{response}[/bold yellow]")

    print("-" * 60)  # separator
    print("[bold blue]Copied to clipboard![bold blue]\n")
    # ----------------------------------------------------------------

    # # APPLY SOME MD FORMATTING
    # # ----------------------------------------------------------------
    # md_prompt = f"###{prompt}"
    # md_response = f"{response}"

    # # PATH
    # # ----------------------------------------------------------------
    # path = "C:/Users/Gero Zayas/Downloads/ChatGPT/"

    # # SAVE RESPONSE TO MARKDOWN FILE
    # # ----------------------------------------------------------------
    # with open(
    #     f"{path}ChatGPT_Interaction_{today}.md", "a", encoding="utf-8"
    # ) as md_file:
    #     md_file.write(markdown(md_prompt))
    #     md_file.write("\n")
    #     md_file.write(markdown(md_response))
    #     md_file.write("\n")
    #     md_file.write(markdown("---"))
    #     md_file.write("\n")


# FINISH PROGRAM
# ----------------------------------------------------------------
bye_string = "\nThis program is finished now. Have a great day"

for word in bye_string.split():
    print()
    print("          " + word)
    time.sleep(0.2)

time.sleep(1)
