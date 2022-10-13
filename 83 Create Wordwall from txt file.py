import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# go to wordwall.net
# go to log in
# go to create activity
# select match up
# type in name in activity title
# copy from text file first column
# paste first column data into keyword column
# copy from text file second column
# paste first column data into definition column
# click on Done


WORDWALL_EMAIL = "gerozayas@gmail.com"
WORDWALL_PASSWORD = "clavegerozayas7"
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

wordwall_website = driver.get("https://wordwall.net/")
time.sleep(3)

create_activity_btn = driver.find_element_by_xpath(
    '//*[@id="outer_wrapper"]/div[1]/div[1]/header/div[1]/a[1]'
)

create_activity_btn.send_keys(Keys.ENTER)

time.sleep(3)
driver.close()
