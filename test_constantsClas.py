from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.passwordConstants import *
import json
import imaplib
import email
from selenium.webdriver.common.keys import Keys

class Test_mailDogrulama():
    def test_linkionaylama(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mail.google.com/mail/u/0/#inbox")
        email_giris=self.waitForElelemetVisible((By.ID, "identifierId"))
        sleep(3)
        email_giris.send_keys(validemail)
        email_giris.click()
        sonraki= self.waitForElelemetVisible((By.XPATH, "//div[@id='identifierNext']/div/button/span"))
        sonraki.click()

        password=self.waitForElelemetVisible((By.CSS_SELECTOR,passwordCSS))
        password.send_keys(validPassword)
        simdi_giris_yap=self.waitForElelemetVisible((By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d"))
        simdi_giris_yap.click()


        # İlk mesajı bulmak için bekleyici oluştur
        window_before = self.driver.window_handles[0]
        sleep(1)
        first_message = self.waitForElelemetVisible((By.XPATH, "//*[@id=':24']"))
        first_message.click()  # İlk mesaja tıkla

        self.driver.execute_script("window.scrollTo(0,200)")
        sleep(2)
        first_messageLink = self.waitForElelemetVisible((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div/div/div/p/span/a"))
        first_messageLink.click()
        sleep(5)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        yeniSifreInput = self.waitForElelemetVisible((By.XPATH,yeniSifreXpath))
        yeniSifreInput.send_keys(yeniSifreBelirleme)
        yeniSifreTekrarInput = self.waitForElelemetVisible((By.XPATH,sifreTekrarXpath))
        yeniSifreTekrarInput.send_keys(yeniSifreBelirleme)
        gonderButon = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss))
        gonderButon.click()

      
        


    def waitForElelemetVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
class Test_notMatchPassword():
    def test_linkionaylama(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mail.google.com/mail/u/0/#inbox")
        email_giris=self.waitForElelemetVisible((By.ID, "identifierId"))
        sleep(3)
        email_giris.send_keys(validemail)
        email_giris.click()
        sonraki= self.waitForElelemetVisible((By.XPATH, "//div[@id='identifierNext']/div/button/span"))
        sonraki.click()

        password=self.waitForElelemetVisible((By.CSS_SELECTOR,passwordCSS))
        password.send_keys(validPassword)
        simdi_giris_yap=self.waitForElelemetVisible((By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d"))
        simdi_giris_yap.click()


        # İlk mesajı bulmak için bekleyici oluştur
        window_before = self.driver.window_handles[0]
        sleep(1)
        first_message = self.waitForElelemetVisible((By.XPATH, "//*[@id=':24']"))
        first_message.click()  # İlk mesaja tıkla

        self.driver.execute_script("window.scrollTo(0,200)")
        sleep(2)
        first_messageLink = self.waitForElelemetVisible((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div/div/div/p/span/a"))
        first_messageLink.click()
        sleep(5)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        yeniSifreInput = self.waitForElelemetVisible((By.XPATH,yeniSifreXpath))
        yeniSifreInput.send_keys(yeniSifreBelirleme)
        yeniSifreTekrarInput = self.waitForElelemetVisible((By.XPATH,sifreTekrarXpath))
        yeniSifreTekrarInput.send_keys(uyumsuzSifre)
        gonderButon = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss))
        gonderButon.click()
        sleep(10)

      
        


    def waitForElelemetVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))