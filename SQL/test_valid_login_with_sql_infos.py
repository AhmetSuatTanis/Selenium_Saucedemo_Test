import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
import pytest
from constants.loginConstants import *


class Test_Login_SQL:

    def waitForElementVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementAvailableForIFrame(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.frame_to_be_available_and_switch_to_it(locator))
    

    def test_valid_login_with_sql(self):

        # Veritabanına bağlan
        conn = sqlite3.connect('C:/sqlitedbs/login.db')  # Veritabanının tam yolunu belirttim.

        # Bağlantı üzerinden bir cursor (imleç) oluştururur
        c = conn.cursor()

        # Veritabanından kullanıcı bilgilerini al
        c.execute("SELECT email, password FROM login")
        user_info = c.fetchall()

        #veri tabanından alınan bilgileri teker teker çeviren for döngüsü
        for email, password in user_info:
            self.driver=webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get("https://tobeto.com/giris")
            emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))

            # database'den gelen e-mail veya password null ise onlara boş String değeri atar. 
            # bunu yapmamızın sebebi send_keys() metodunun null hatası vermesi.
            if not email:
               email = ""
            if not password:
               password = ""

            emailInput.send_keys(email)
            passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
            passwordInput.send_keys(password)
            loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
            loginButton.click()

            # Boş bırakılan yerlerin altında uyarı mesajları çıktığı için if else bloğuyla assertionları kontrol ederiz.
            if not email and not password:
                assert emailError_Message==self.waitForElementVisible((By.CSS_SELECTOR,emailErrorMessage_CSS)).text,f"'{emailError_Message}' ifadesi bulunamadı."
                assert passwordError_Message==self.waitForElementVisible((By.CSS_SELECTOR,passwordErrorMessage_CSS)).text,f"'{emailError_Message}' ifadesi bulunamadı."
            # uyari pop-up mesajları için bu bloğa girer ve koşullardan biri bile karşılansa assertion true verir ve testimiz geçer       
            else: 
                assert any([successLogin_message== self.waitForElementVisible((By.CSS_SELECTOR,successLogin_CSS)).text , invalidEmailOrPassword_errorMessage==self.waitForElementVisible((By.CSS_SELECTOR,invalidEmailOrPassword_errorMessage_CSS)).text , deactiveUserLogin_errorMessage==self.waitForElementVisible((By.CSS_SELECTOR,deactiveUserLogin_errorMessage_CSS)).text]), "Beklenen mesajlar bulunamadı."
            
            sleep(2)
            self.driver.quit()

            
            
            

    


