from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
import json 
from constants.loginConstants import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

class Test_Login:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(login_URL) #constants klasörü açarak içine değişkenler oluşturduk ordan çektik

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementAvailableForIFrame(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.frame_to_be_available_and_switch_to_it(locator))
    
    def waitForElementClickable(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
    
    def test_valid_login(self):
        emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))
        passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
        loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(emailInput,userEmail)
        actions.send_keys_to_element(passwordInput,userPassword)
        actions.click(loginButton)
        actions.perform()
        assert successLogin_message== self.waitForElementVisible((By.CSS_SELECTOR,successLogin_CSS)).text, f"'{successLogin_message} ifadesi bulunamadı'"
        sleep(3)

    def test_blankEmailAndPassword_login(self):
        emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))
        passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
        loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(emailInput,"")
        actions.send_keys_to_element(passwordInput,"")
        actions.click(loginButton)
        actions.perform()
        assert emailError_Message==self.waitForElementVisible((By.CSS_SELECTOR,emailErrorMessage_CSS)).text,f"'{emailError_Message}' ifadesi bulunamadı."
        assert passwordError_Message==self.waitForElementVisible((By.CSS_SELECTOR,passwordErrorMessage_CSS)).text,f"'{emailError_Message}' ifadesi bulunamadı."
        sleep(3)

    def test_invalidPassword_errorMessage(self):
        emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))
        passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
        loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(emailInput,userEmail)
        actions.send_keys_to_element(passwordInput,userPassword+"123")
        actions.click(loginButton)
        actions.perform()
        assert invalidEmailOrPassword_errorMessage==self.waitForElementVisible((By.CSS_SELECTOR,invalidEmailOrPassword_errorMessage_CSS)).text,f"'{invalidEmailOrPassword_errorMessage}' ifadesi bulunamadı."
        sleep(3)

    def test_invalidEmail_errorMessage(self):
        emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))
        passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
        loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(emailInput,userEmail+".com")
        actions.send_keys_to_element(passwordInput,userPassword)
        actions.click(loginButton)
        actions.perform()
        assert invalidEmailOrPassword_errorMessage==self.waitForElementVisible((By.CSS_SELECTOR,invalidEmailOrPassword_errorMessage_CSS)).text,f"'{invalidEmailOrPassword_errorMessage}' ifadesi bulunamadı."
        sleep(3)

    def test_deactiveUser_login(self):
        emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))
        passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
        loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(emailInput,deactiveUserEmail)
        actions.send_keys_to_element(passwordInput,deactiveUserPassword)
        actions.click(loginButton)
        actions.perform()
        assert deactiveUserLogin_errorMessage==self.waitForElementVisible((By.CSS_SELECTOR,deactiveUserLogin_errorMessage_CSS)).text,f"'{deactiveUserLogin_errorMessage}' ifadesi bulunamadı."
        sleep(3)

    
        
        

        