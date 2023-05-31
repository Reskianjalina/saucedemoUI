import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self): #test cases 1
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()

    def test_a_failed_login_empty_email(self): #test cases 2
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Username is required", error_message)

    def test_a_failed_login_empty_password(self): #test cases 3
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Password is required", error_message)
    
    def test_a_failed_login_empty_email_and_password(self): #test cases 4
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Username is required", error_message)

    def test_a_invalid_email_login(self): #test cases 5
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("mona_mona")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_message)

def test_a_invalid_password_login(self): #test cases 6
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_number")
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_message)

if __name__ == '__main__':
    unittest.main()