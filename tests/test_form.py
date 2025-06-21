from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_form_submission():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # For Jenkins environment
    driver = webdriver.Chrome(options=options)
    driver.get("https://demoapps.qspiders.com/ui?scenario=1")

    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john@example.com")
    driver.find_element(By.ID, "password").send_keys("secret")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    success_msg = driver.find_element(By.ID, "messageOne").text
    assert "Registered successfully" in success_msg

    driver.quit()
