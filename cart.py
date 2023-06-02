import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObject.locator import elem
import baselogin

class TestCart(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_cart(self): #test cases 1
        baseUrl = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(baseUrl)
        baselogin.test_a_success_login(driver)
        driver.find_element(By.CSS_SELECTOR, elem.addCartBakpack).click()
        driver.find_element(By.CLASS_NAME, elem.linkCartBakpack).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "/cart.html")
    
if __name__ == '__main__':
    unittest.main()