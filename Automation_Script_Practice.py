import cv2
from gui_automation import GuiAuto

# THIS SCRIPT OPENS GOOGLE WINDOW, NOTES OR Z APPLICATION FOLLOWING THE USER PROMPT COMMANDS

# Dictionary of possibile commands
command_dict = {
    "o g": "open_google",
    "o z": "open_z",
    "o n": "open_notes",
}

program_run = True


while program_run:

    # Receives imput form as command
    user_command = input("insert command e.g. [o g] or [o z] or h for help:")

    if user_command == "o g":
        image_path = "open_google.png"
    elif user_command == "o z":
        image_path = "open_z.png"
    elif user_command == "o n":
        image_path = "open_notes.png"
    elif user_command == "h":
        for k, v in command_dict.items():
            print(k, "-----", v)
            program_run = False
    else:
        print("INCORRECT INPUT")
        program_run = False

    ga = GuiAuto()
    if ga.detect(cv2.imread(image_path), 0.8):
        ga.click()

    user_answer = input("Want to run again [y] or [n]:")
    if user_answer == "y":
        program_run = True
    else:
        print("Bye Bye")
        program_run = False
