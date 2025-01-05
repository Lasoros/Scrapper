

from selenium.webdriver import webdriver
from selenium.webdriver.chrome.service import Service


def scrape_site_test(website):
    print("Launching Chrome . . .")

    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Loaded Page. . .")
        html = driver.page_source

        return html
    finally:
        driver.quit()