from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


driver.get("hidden for reasons")


element = driver.find_element(By.CSS_SELECTOR, "ocode")

after_content = driver.execute_script("""
    var element = arguments[0];
    var style = window.getComputedStyle(element, ':after');
    return style.getPropertyValue('content');
""", element)

print("After Content:", after_content)


driver.quit()