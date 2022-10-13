import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


WORDWALL_EMAIL = "gerozayas@gmail.com"
WORDWALL_PASSWORD = "clavegerozayas7"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

# go to wordwall.net -> log in

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

wordwall_website = driver.get("https://wordwall.net/account/login")
time.sleep(3)


email = driver.find_element(By.ID, "Email")
password = driver.find_element(By.ID, "Password")
email.send_keys(WORDWALL_EMAIL)
time.sleep(3)
password.send_keys(WORDWALL_PASSWORD)
time.sleep(3)

log_in_btn = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[2]/form/div[4]/div/button"
)

log_in_btn.click()
time.sleep(3)

# go to create activity


# select match up
# type in name in activity title
# copy from text file first column
# paste first column data into keyword column
# copy from text file second column
# paste first column data into definition column
# click on Done
