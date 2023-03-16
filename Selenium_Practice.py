from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.google.com")
time.sleep(2)

accept_button = driver.find_element(by="id", value="L2AGLb")
accept_button.click()

time.sleep(2)

search_box = driver.find_element(by="name", value="q")
search_box.send_keys("Selenium Python")
search_box.submit()

# driver.quit()
