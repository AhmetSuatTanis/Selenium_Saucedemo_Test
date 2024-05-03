from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.serftifikalarimConstants import *
#pre-conditions kısmı için giriş yapma, bilgiler ve locate pathleri için loginConstants import edildi.
from constants.loginConstants import *
from selenium.webdriver.common.keys import Keys
import keyboard

class Test_Sertifikalarim:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(giris_URL)
        
    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementsVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))    

    def pre_condition(self):
        emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))
        passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
        loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(emailInput,userEmail)
        actions.send_keys_to_element(passwordInput,userPassword)
        actions.click(loginButton)
        actions.perform()
        sleep(0.1)
        successPopupMessageClose=self.waitForElementVisible((By.CSS_SELECTOR,successPopupMessage_CSS))
        successPopupMessageClose.click()
        profilDropdownMenu=self.waitForElementVisible((By.CSS_SELECTOR,profilDropdownMenu_CSS))
        profilDropdownMenu.click()
        profileInformationButton=self.waitForElementVisible((By.XPATH,profileInformationButton_xpath))
        profileInformationButton.click()    

    

    def test_certificate_adding_deleting_downloading(self):
        self.pre_condition()
        MyCertificatesButton=self.waitForElementVisible((By.XPATH,MyCertificatesButton_xpath))
        MyCertificatesButton.click()
        sleep(2)
        fileDownloadButton=self.waitForElementVisible((By.CSS_SELECTOR,fileDownloadButton_CSS))
        fileDownloadButton.click()
        sleep(2)
        viewButton=self.waitForElementVisible((By.CSS_SELECTOR,viewButton_CSS))
        viewButton.click()
        sleep(2)
        #Burada keyboard modülünü kullanarak keydoard ile dosya konumunu yazdırıp o şekilde dosya yükleme yaptırıyoruz.
        keyboard.write(r"C:\Users\AHMET\Desktop\SendFile\tobeto.jpg")
        sleep(2)
        keyboard.press("enter")
        cancelButton=self.waitForElementVisible((By.CSS_SELECTOR,cancelButton_CSS))
        cancelButton.click()
        viewButton=self.driver.find_element(By.XPATH, viewButton_xpath)
        sleep(2)
        # send_keys() metodu ile Excel file göndermeyi deniyoruz. 
        viewButton.send_keys("C:\\Users\\AHMET\\Desktop\\SendFile\\tobeto.xlsx")
        warningMessage=self.waitForElementVisible((By.CSS_SELECTOR,warningMessage_CSS))
        assert warningMessageText==warningMessage.text, f"'{warningMessageText}' ifadesi bulunamadı."
        sleep(2)
        viewButton=self.driver.find_element(By.XPATH, viewButton_xpath)
        # send_keys() metodu ile png file göndermeyi deniyoruz. 
        viewButton.send_keys("C:\\Users\\AHMET\\Desktop\\SendFile\\html.png")
        sleep(2)
        uploadButton=self.waitForElementVisible((By.XPATH,uploadButton_xpath))
        uploadButton.click()
        sleep(2)
        downloadButton=self.waitForElementVisible((By.XPATH,downloadButton_xpath))
        downloadButton.click()
        sleep(2)
        deleteButton=self.waitForElementVisible((By.XPATH,deleteButton_xpath))
        deleteButton.click()
        sleep(2)
        noButton=self.waitForElementVisible((By.XPATH,noButton_xpath))
        noButton.click()
        sleep(2)
        deleteButton=self.waitForElementVisible((By.XPATH,deleteButton_xpath))
        deleteButton.click()
        sleep(2)
        yesButton=self.waitForElementVisible((By.XPATH,yesButton_xpath))
        yesButton.click()
        successfulDeletePopUpMessage=self.waitForElementVisible((By.XPATH,successfulDeletePopUpMessage_xpath))
        assert expectedSuccessfulDeletePopUpMessage in successfulDeletePopUpMessage.text, f"'{expectedSuccessfulDeletePopUpMessage}' ifadesi bulunamadı."
        sleep(2)



        
    
        




        
        
        
