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
        profilBilgileriButton=self.waitForElementVisible((By.XPATH,profilBilgileriButonu_xpath))
        profilBilgileriButton.click()
    
    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementsVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def test_sertifika_ekleme_silme_indirme(self):
        sertifikalarimButonu=self.waitForElementVisible((By.XPATH,sertifikalarimButonu_xpath))
        sertifikalarimButonu.click()
        sleep(2)
        dosyaYuklemeButonu=self.waitForElementVisible((By.CSS_SELECTOR,dosyaYuklemeButonu_CSS))
        dosyaYuklemeButonu.click()
        sleep(2)
        gozatButonu=self.waitForElementVisible((By.CSS_SELECTOR,gozatButonu_CSS))
        gozatButonu.click()
        sleep(2)
        #Burada keyboard modülünü kullanarak keydoard ile dosya konumunu yazdırıp o şekilde dosya yükleme yaptırıyoruz.
        keyboard.write(r"C:\Users\AHMET\Desktop\SendFile\tobeto.jpg")
        sleep(2)
        keyboard.press("enter")
        iptalButonu=self.waitForElementVisible((By.CSS_SELECTOR,iptalButonu_CSS))
        iptalButonu.click()
        gozatButonu=self.driver.find_element(By.XPATH, gozatButonu_xpath)
        sleep(2)
        # send_keys() metodu ile Excel file göndermeyi deniyoruz. 
        gozatButonu.send_keys("C:\\Users\\AHMET\\Desktop\\SendFile\\tobeto.xlsx")
        uyariMesaji=self.waitForElementVisible((By.CSS_SELECTOR,uyariMesajiText_CSS))
        assert uyariMesajiText==uyariMesaji.text, f"'{uyariMesajiText}' ifadesi bulunamadı."
        sleep(2)
        gozatButonu=self.driver.find_element(By.XPATH, gozatButonu_xpath)
        # send_keys() metodu ile png file göndermeyi deniyoruz. 
        gozatButonu.send_keys("C:\\Users\\AHMET\\Desktop\\SendFile\\html.png")
        sleep(2)
        yukleButonu=self.waitForElementVisible((By.XPATH,yukleButonu_xpath))
        yukleButonu.click()
        sleep(2)
        indirButonu=self.waitForElementVisible((By.XPATH,indirButonu_xpath))
        indirButonu.click()
        sleep(2)
        silmeButonu=self.waitForElementVisible((By.XPATH,silmeButonu_xpath))
        silmeButonu.click()
        sleep(2)
        hayirButonu=self.waitForElementVisible((By.XPATH,hayirButonu_xpath))
        hayirButonu.click()
        sleep(2)
        silmeButonu=self.waitForElementVisible((By.XPATH,silmeButonu_xpath))
        silmeButonu.click()
        sleep(2)
        evetButonu=self.waitForElementVisible((By.XPATH,evetButonu_xpath))
        evetButonu.click()
        basariliSilmePopUpMesaji=self.waitForElementVisible((By.XPATH,basariliSilmePopUpMesaji_xpath))
        assert beklenenBasariliSilmePopUpMesaji in basariliSilmePopUpMesaji.text, f"'{beklenenBasariliSilmePopUpMesaji}' ifadesi bulunamadı."
        sleep(2)



        
    
        




        
        
        
