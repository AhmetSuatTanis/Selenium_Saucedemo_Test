from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.RegisterConstants import *
import json 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


class Test_Register:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tobeto.com/giris") #constants klasörü açarak içine değişkenler oluşturduk ordan çektik

    def teardown_method(self):
        self.driver.quit()
    
    def waitForElementVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementAvailableForIFrame(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.frame_to_be_available_and_switch_to_it(locator))
    
    def waitForElementClickable(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    
    def test_valid_register(self):
        sifreYenilemeButton=self.waitForElementVisible((By.CSS_SELECTOR,".d-block.mt-5.text-decoration-none.text-muted"))
        sleep(5)
        sifreYenilemeButton.click()
        sleep(10)