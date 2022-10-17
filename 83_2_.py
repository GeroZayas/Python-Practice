# IDEA:
# Write a script that goes file for file inside folder and creates a wordwall for each file.

# Also, sometimes it appears to need the utf-8 *encoding* to work properly.
# Which I took away


import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip

start = time.time()


WORDWALL_EMAIL = "gerozayas@gmail.com"
WORDWALL_PASSWORD = "clavegerozayas7"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

print("HELLO! Welcome to the Wordwall Creator")
print("Make sure the text file is in the same folder as this script!")
print(":)")


NAME_OF_FOLDER = input("insert name of FOLDER: ")

# TODO open all file names from file with names
# IDEA: use os.listdir() to get all file names from folder
# create function for all this and then run the function with every file name


# go to wordwall.net -> log in


def create_worwall(file_name):

    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    wordwall_website = driver.get("https://wordwall.net/account/login")
    time.sleep(2)

    email = driver.find_element(By.ID, "Email")
    password = driver.find_element(By.ID, "Password")
    email.send_keys(WORDWALL_EMAIL)
    time.sleep(1)
    password.send_keys(WORDWALL_PASSWORD)
    time.sleep(1)

    log_in_btn = driver.find_element(
        By.XPATH, "/html/body/div[2]/div[2]/form/div[4]/div/button"
    )

    log_in_btn.click()
    time.sleep(2)

    # go to create activity

    # select match up

    match_up_template = driver.get(
        "https://wordwall.net/create/entercontent?templateId=3"
    )

    time.sleep(2)

    # type in name in activity title

    activity_title = driver.find_element(By.CLASS_NAME, "js-activity-title")

    activity_title.send_keys(Keys.CONTROL + "a")
    activity_title.send_keys(Keys.DELETE)
    time.sleep(1)

    # # get activity title from file
    # with open(f"{FILE}", "r") as file:
    #     activity_name = file.readlines()[0]

    # TODO the idea here now is to loop over the file and automatically upload each one
    # one by one
    FILE = file_name

    activity_title_string = FILE[:-4].split("_")[0]
    activity_level_string = FILE[:-4].split("_")[1]

    # print(f"{activity_title_string} - {activity_level_string}")

    activity_title.send_keys(
        f"{activity_title_string} - Level {activity_level_string} from Memrise"
    )

    # copy from text file first column

    # paste first column data into keyword column

    keyword_input = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div[2]/div[6]/div[2]/div[3]/div/div[1]/div[3]/div[1]/div[5]/div",
    )

    # ***** DETERMINE LIST LENGTH *****
    list_length = 0

    with open(f"./{NAME_OF_FOLDER}/{FILE}", "r") as file:
        list_length += len(file.readlines())

    list_length = list_length // 2 - 2
    # print(list_length)

    # ***** END of DETERMINE LIST LENGTH *****

    with open(f"./{NAME_OF_FOLDER}/{FILE}", "r", encoding="utf-8") as file:
        first_column = file.readlines()[4 : list_length + 4]

    string_first_column = "".join(first_column)

    pyperclip.copy(string_first_column)

    keyword_input.send_keys(Keys.CONTROL + "v")

    time.sleep(2)

    # copy from text file second column
    # paste first column data into definition column

    definition_input = driver.find_element(
        By.XPATH,
        '//*[@id="editor_component_0"]/div[3]/div/div[1]/div[3]/div[2]/div[4]/div',
    )

    with open(f"./{NAME_OF_FOLDER}/{FILE}", "r", encoding="utf-8") as file:
        second_column = file.readlines()[list_length + 5 :]

    string_second_column = "".join(second_column)

    pyperclip.copy(string_second_column)

    definition_input.send_keys(Keys.CONTROL + "v")

    time.sleep(2)

    # click on Done

    done_btn = driver.find_element(By.CLASS_NAME, "default-btn.large.js-done-button")
    done_btn.click()

    end = time.time()

    print("TOTAL TIME OF EXECUTION:", int(end - start), "seconds")


names_of_files = os.listdir(f"./{NAME_OF_FOLDER}")


print("**" * 20)
print(names_of_files)

for file in names_of_files:
    create_worwall(file)
