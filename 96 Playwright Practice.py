from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # NOTE that we use headless=False so we can actually see the browser
    # since by default headless is set to True
    browser = p.chromium.launch(headless=False, slow_mo=50)
    # we now need a page object so we can interact with different things
    page = browser.new_page()
    page.goto("https://www.google.com/")
    # to type into a box we use .fill()
    page.fill("input#gLFyf gsfi", value="demo")
    page.click("input#gNO89b")
