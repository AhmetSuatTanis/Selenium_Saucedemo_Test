from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.common.exceptions import TimeoutException
import pytest
import openpyxl
from constants.passwordConstants import *
import json
import imaplib
import email
from selenium.webdriver.common.keys import Keys
from test_constantsClas import *
from selenium.webdriver.common.alert import Alert

class Test_Sifre():
      def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

      def teardown_method(self):
        self.driver.quit()

      def test_invalidMail(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(gecersizformatmail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         gecersizformatMailText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
         assert gecersizformatMailText.text == gecersizformattext
      
      def test_succesPasswordReset(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(validemail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         Test_mailDogrulama().test_linkionaylama()
         sleep(10)

         
      
        #  succesResetText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
        #  assert succesResetText.text == sifreSifirlamaBasariliText
        # bununun yerine yeni password ile giris yapalim


      
      def test_unregisteredMail(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(unregisteredMail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         unregisteredText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
         assert unregisteredText.text == gecersizformattext
       
      def test_notMatchPassword(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(validemail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         Test_notMatchPassword().test_linkionaylama()

         try:
          notMatchPasswordText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
          assert notMatchPasswordText.text == sifreEslesmediText
        
         except TimeoutException:
          pytest.fail("Success message did not appear within 10 seconds")

         

      def waitForElelemetVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))