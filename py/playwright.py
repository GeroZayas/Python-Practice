from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# Mimic a common Chrome User-Agent on Windows 10
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


# Disable automation detection (important for realism)
options.add_argument("--disable-blink-features=AutomationControlled")

# Exclude some WebDriver properties (helps evade detection)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


# Optional: Headless mode if you don't need a visible browser window.  Remove for a visible browser.  May affect realism depending on the site.
# options.add_argument("--headless")


driver = webdriver.Chrome(options=options)


# Example Usage (replace with your actual URL)
driver.get(
    "https://docs.google.com/spreadsheets/d/1AStOsEeBOsk6b0OhSMRnjXSYmBL6jOyboYSofpWVFas/edit?gid=1736954774#gid=1736954774"
)

# Execute JavaScript (if needed to ensure rendering)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll to bottom

# Access rendered content
print(driver.page_source)


driver.quit()
