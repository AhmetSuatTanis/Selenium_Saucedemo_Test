import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test_Selenium_Ide():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_blank_login(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required"

    def test_blank_password_login(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Password is required"

    def test_lockedUserlogin(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("locked_out_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Sorry, this user has been locked out."

    def test_valid_login(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".app_logo")))
        assert self.driver.find_element(By.CSS_SELECTOR, ".app_logo").text == "Swag Labs"

    def test_addToCartProduct(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").text == "1"

    def test_removeProductFromCart(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").text == "1"
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()
        elements = self.driver.find_elements(By.XPATH, "//span[@class=\'shopping_cart_badge\']")
        assert len(elements) == 0

    def test_checkoutProduct(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"checkout\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"firstName\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("Ahmet")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"lastName\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("tanis")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"postalCode\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("34212")
        self.driver.find_element(By.CSS_SELECTOR, "form").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"continue\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"finish\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"complete-header\"]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"complete-header\"]").text == "Thank you for your order!"
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]")))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
        
        


    
        
    
        



        

        
        
        
        