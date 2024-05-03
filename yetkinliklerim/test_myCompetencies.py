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

    def test_competence_add(self):
        self.pre_condition()
        myCompetenciesButton=self.waitForElementVisible((By.XPATH,myCompetenciesButton_xpath))
        myCompetenciesButton.click()
        competencySelectButton=self.waitForElementVisible((By.CSS_SELECTOR,competencySelectButton_CSS))
        competencySelectButton.click()
        sleep(1)
        #burada locator verirken sona yetkinliklerin hangi sırada olanını eklemek istersem onu eklemiş oldum. "0" ilk sıradaki yetkinliği temsil ediyor.
        competenceSelection1=self.waitForElementVisible((By.CSS_SELECTOR,competenceSelection1_CSS+"0"))
        competenceSelection1.click()
        sleep(1)
        saveButton=self.waitForElementVisible((By.CSS_SELECTOR,saveButton_CSS))
        saveButton.click()
        sleep(2)
        #kaç tane yetkinlike eklendiyse onları liste halinde alan locator. waitForElementsVisible()
        addedCompetency=self.waitForElementVisible((By.XPATH,addedCompetency_xpath))
        addedCompetencies=self.waitForElementsVisible((By.CSS_SELECTOR,addedCompetencies_CSS))
        assert any(addedCompetency.text == competence.text for competence in addedCompetencies), f" yetenek bulunamadı."
        sleep(2)

    def test_competence_delete(self):
        sleep(1)
        self.test_competence_add()
        deleteButton=self.waitForElementVisible((By.CSS_SELECTOR,deleteButton_CSS))
        deleteButton.click()
        noButton=self.waitForElementVisible((By.CSS_SELECTOR,noButton_CSS))
        noButton.click()
        deleteButton.click()
        yesButton=self.waitForElementVisible((By.CSS_SELECTOR,yesButton_CSS))
        yesButton.click()
        actualSuccessfulDeletePopUpMessage=self.waitForElementVisible((By.CSS_SELECTOR,successfulDeletePopUpMessage_CSS))
        assert expectedSuccessfulDeletePopUpMessage in actualSuccessfulDeletePopUpMessage.text, f"'{expectedSuccessfulDeletePopUpMessage}' ifadesi bulunamadı."
        sleep(2)
        #Bu kod bloğu, belirtilen CSS selector'a sahip bir element bulunamazsa NoSuchElementException veya TimeoutException  hatası alır ve bu durumda True döndürür. 
        # try:
        #     element = self.waitForElementVisible((By.CSS_SELECTOR, eklenenYetkinlikler_CSS))
        #     assert element.is_displayed()
        # except (NoSuchElementException, TimeoutException):
        #     assert True

    def test_bosBirakilanYerler_hataMesajlari(self):
        self.pre_condition()
        myCompetenciesButton=self.waitForElementVisible((By.XPATH,myCompetenciesButton_xpath))
        myCompetenciesButton.click()
        saveButton=self.waitForElementVisible((By.CSS_SELECTOR,saveButton_CSS))
        saveButton.click()
        errorMessage=self.waitForElementVisible((By.CSS_SELECTOR,errorMessage_CSS))
        assert expectedErrorMessage in errorMessage.text, f"'{expectedErrorMessage}' ifadesi bulunamadı."
        sleep(2)
        






        
        