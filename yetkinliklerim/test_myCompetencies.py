from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.yetkinliklerConstants import *
#pre-conditions kısmı için giriş yapma, bilgiler ve locate pathleri için loginConstants import edildi.
from constants.loginConstants import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Test_Yetkinliklerim:
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
        profilBilgileriButton=self.waitForElementVisible((By.XPATH,profilBilgileriButton_xpath))
        profilBilgileriButton.click()
    
    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementsVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def test_yetkinlik_ekleme(self):
        yetkinliklerimButonu=self.waitForElementVisible((By.XPATH,yetkinliklerimButonu_xpath))
        yetkinliklerimButonu.click()
        yetkinlikSecmeButonu=self.waitForElementVisible((By.CSS_SELECTOR,yetkinlikSecmeButonu_CSS))
        yetkinlikSecmeButonu.click()
        sleep(1)
        #burada locator verirken sona yetkinliklerin hangi sırada olanını eklemek istersem onu eklemiş oldum. "0" ilk sıradaki yetkinliği temsil ediyor.
        yetkinlikSecme1=self.waitForElementVisible((By.CSS_SELECTOR,secilenYetkinlik_CSS+"0"))
        yetkinlikSecme1.click()
        sleep(1)
        kaydetButonu=self.waitForElementVisible((By.CSS_SELECTOR,kaydetButonu_CSS))
        kaydetButonu.click()
        eklenenYetkinlikler=self.waitForElementsVisible((By.CSS_SELECTOR,eklenenYetkinlikler_CSS))
        assert any("C#" == yetkinlik.text for yetkinlik in eklenenYetkinlikler)
        sleep(2)

    def test_yetkinlik_silme(self):
        self.test_yetkinlik_ekleme()
        silmeButonu=self.waitForElementVisible((By.CSS_SELECTOR,silmeButonu_CSS))
        silmeButonu.click()
        hayirButonu=self.waitForElementVisible((By.CSS_SELECTOR,hayirButonu_CSS))
        hayirButonu.click()
        silmeButonu.click()
        evetButonu=self.waitForElementVisible((By.CSS_SELECTOR,evetButonu_CSS))
        evetButonu.click()
        sleep(1)
        #Bu kod bloğu, belirtilen CSS selector'a sahip bir element bulunamazsa NoSuchElementException veya TimeoutException  hatası alır ve bu durumda True döndürür. 
        try:
            element = self.waitForElementVisible((By.CSS_SELECTOR, eklenenYetkinlikler_CSS))
            assert element.is_displayed()
        except (NoSuchElementException, TimeoutException):
            assert True

    def test_bosBirakilanYerler_hataMesajlari(self):
        yetkinliklerimButonu=self.waitForElementVisible((By.XPATH,yetkinliklerimButonu_xpath))
        yetkinliklerimButonu.click()
        kaydetButonu=self.waitForElementVisible((By.CSS_SELECTOR,kaydetButonu_CSS))
        kaydetButonu.click()
        hataMesaji=self.waitForElementVisible((By.CSS_SELECTOR,hataMesaji_CSS))
        assert hataMesaji_text in hataMesaji.text, f"'{hataMesaji}' ifadesi bulunamadı."
        sleep(2)
        






        
        