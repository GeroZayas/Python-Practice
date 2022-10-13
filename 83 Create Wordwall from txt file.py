from ast import keyword
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip

WORDWALL_EMAIL = "gerozayas@gmail.com"
WORDWALL_PASSWORD = "clavegerozayas7"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

# go to wordwall.net -> log in

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

match_up_template = driver.get("https://wordwall.net/create/entercontent?templateId=3")

time.sleep(2)


# type in name in activity title

activity_title = driver.find_element(By.CLASS_NAME, "js-activity-title")
time.sleep(1)

activity_title.send_keys(Keys.CONTROL + "a")
activity_title.send_keys(Keys.DELETE)
time.sleep(1)

activity_title.send_keys("THIS IS A TEST")

# copy from text file first column


# paste first column data into keyword column

example_dict = {"one": "uno", "two": "dos", "three": "tres"}
example_list = ["one", "two", "three"]


keyword_input = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div[2]/div[6]/div[2]/div[3]/div/div[1]/div[3]/div[1]/div[5]/div",
)

# TODO make sure I control + c the keywords for this to work
# TODO I just have to make sure to have what i want in clipboard (copied)

list_length = 29

with open("test.txt", "r", encoding="utf-8") as file:
    first_column = file.readlines()[4 : list_length + 4]

string_first_column = "".join(first_column)

pyperclip.copy(string_first_column)

keyword_input.send_keys(Keys.CONTROL + "v")

time.sleep(1)

# copy from text file second column
# paste first column data into definition column


definition_input = driver.find_element(
    By.XPATH,
    '//*[@id="editor_component_0"]/div[3]/div/div[1]/div[3]/div[2]/div[4]/div',
)


definition_input.send_keys("DEFINITION")
time.sleep(1)

definition_input.send_keys(Keys.ENTER)
time.sleep(1)


# click on Done
