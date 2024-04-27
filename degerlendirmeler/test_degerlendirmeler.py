from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.degerlendirmelerConstants import *
#pre-conditions kısmı için giriş yapma, bilgiler ve locate pathleri için loginConstants import edildi.
from constants.loginConstants import *
from selenium.webdriver.common.keys import Keys

class Test_Degerlendirmeler:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(giris_URL)
        emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))
        passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
        loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(emailInput,userEmail)
        actions.send_keys_to_element(passwordInput,userPassword)
        actions.click(loginButton)
        actions.perform()
        successPopupMessageClose=self.waitForElementVisible((By.CSS_SELECTOR,successPopupMessage_CSS))
        successPopupMessageClose.click()
        

        
    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementsVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))


    def test_degerlendirmeler(self):
        degerlendirmelerButonu=self.waitForElementVisible((By.XPATH,degerlendirmelerButonu_xpath))
        degerlendirmelerButonu.click()
        tobetoBasligi=self.waitForElementVisible((By.CSS_SELECTOR,tobetoBasligiText_CSS))
        assert tobetoBasligiText == tobetoBasligi.text, f"'{tobetoBasligiText}' ifadesi bulunamadı."
        baslaButonu=self.waitForElementVisible((By.CSS_SELECTOR,baslaButonu_CSS))
        baslaButonu.click()
        assert isteBasariModeli_link==self.driver.current_url
        degerlendirmeyeBaslaButonu=self.waitForElementVisible((By.CSS_SELECTOR,degerlendirmeyeBaslaButonu_CSS))
        actions = ActionChains(self.driver)
        actions.move_to_element(degerlendirmeyeBaslaButonu).perform()
        degerlendirmeyeBaslaButonu.click()
        sleep(1)