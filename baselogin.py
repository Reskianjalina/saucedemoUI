import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObject.locator import elem
from PageObject.dataInput import inputan

def test_a_success_login(driver): #test cases 1
    baseUrl = "https://www.saucedemo.com"
    driver.get(baseUrl)
    driver.find_element(By.ID, elem.username).send_keys(inputan.validUser)
    driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPassword)
    driver.find_element(By.NAME, elem.loginButton).click()

