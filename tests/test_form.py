from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_form_submission():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("https://demoapps.qspiders.com/ui?scenario=1")

    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("John Doe")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("john@example.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)
    driver.quit()

