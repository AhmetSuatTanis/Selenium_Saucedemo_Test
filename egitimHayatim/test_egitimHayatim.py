from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.egitimHayatimConstanst import *
from constants.loginConstants import *
from selenium.webdriver.common.keys import Keys

class Test_Egitim_Hayatim:
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
        profilDropdownMenu=self.waitForElementVisible((By.CSS_SELECTOR,profilDropdownMenu_CSS))
        profilDropdownMenu.click()
        profilBilgileriButton=self.waitForElementVisible((By.XPATH,profilBilgileriButton_xpath))
        profilBilgileriButton.click()
        egitimHayatimButonu=self.waitForElementVisible((By.XPATH,egitim_Hayatim_xpath))
        egitimHayatimButonu.click()

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
  

    def test_egitimBilgileriGuncelleme(self):
        egitimHayatimButonu=self.waitForElementVisible((By.XPATH,egitim_Hayatim_xpath))
        egitimHayatimButonu.click()
        egitimDurumuButonu=self.waitForElementVisible((By.CSS_SELECTOR,egitimDurumu_CSS))
        egitimDurumuButonu.click()
        egitimSecimi=self.waitForElementVisible((By.CSS_SELECTOR,egitimSecimi_CSS))
        egitimSecimi.click()
        universityInputBox=self.waitForElementVisible((By.XPATH,universityInputBox_xpath))
        departmentInputBox=self.waitForElementVisible((By.XPATH,departmentInputBox_xpath))
        startDateInputBox=self.waitForElementVisible((By.XPATH,startDate_xpath))
        finishtDateInputBox=self.waitForElementVisible((By.XPATH,finishDate_xpath))
        saveButton=self.waitForElementVisible((By.XPATH,saveButton_xpath))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(universityInputBox,universityInfo)
        actions.send_keys(Keys.ENTER)
        actions.send_keys_to_element(departmentInputBox,departmentInfo)
        actions.send_keys(Keys.ENTER)
        actions.send_keys_to_element(startDateInputBox,startDate)
        actions.send_keys(Keys.ENTER)
        actions.send_keys_to_element(finishtDateInputBox,finishDate)
        actions.send_keys(Keys.ENTER)
        actions.click(saveButton)
        actions.perform()
        successMessageText=self.waitForElementVisible((By.CSS_SELECTOR,successMessage_CSS))
        assert successMessageText.text==successMessage,f"'{successMessage}' ifadesi bulunamadı."
        educationVerify=self.waitForElementVisible((By.XPATH,educationVerify_xpath))
        assert educationVerify.text==universityInfo,f"'{universityInfo}' ifadesi bulunamadı."
        sleep(5)
        
        




