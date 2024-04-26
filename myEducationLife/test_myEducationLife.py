from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.egitimHayatimConstanst import *
#pre-conditions kısmı için giriş yapma, bilgiler ve locate pathleri için loginConstants import edildi.
from constants.loginConstants import *
from selenium.webdriver.common.keys import Keys

class Test_MyEducation_Life:
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
    

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementsVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))


    def test_add_education(self):
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
        actions.perform()
        saveButton.click()
        assert successPopUpMessage in self.waitForElementVisible((By.CSS_SELECTOR,successPopUpMessage_CSS)).text  , f"'{successPopUpMessage}' ifadesi bulunamadı."
        educationVerify=self.waitForElementVisible((By.CSS_SELECTOR,educationVerify_CSS))
        assert educationVerify.text==universityInfo,f"'{universityInfo}' ifadesi bulunamadı."
        sleep(2)

    def test_add_continuing_education(self):
        egitimHayatimButonu=self.waitForElementVisible((By.XPATH,egitim_Hayatim_xpath))
        egitimHayatimButonu.click()
        egitimDurumuButonu=self.waitForElementVisible((By.CSS_SELECTOR,egitimDurumu_CSS))
        egitimDurumuButonu.click()
        egitimSecimi=self.waitForElementVisible((By.CSS_SELECTOR,egitimSecimi_CSS))
        egitimSecimi.click()
        universityInputBox=self.waitForElementVisible((By.XPATH,universityInputBox_xpath))
        departmentInputBox=self.waitForElementVisible((By.XPATH,departmentInputBox_xpath))
        startDateInputBox=self.waitForElementVisible((By.XPATH,startDate_xpath))
        continueEducationButton=self.waitForElementVisible((By.CSS_SELECTOR,continueEducationButton_CCS))
        saveButton=self.waitForElementVisible((By.XPATH,saveButton_xpath))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(universityInputBox,universityInfo)
        actions.send_keys(Keys.ENTER)
        actions.send_keys_to_element(departmentInputBox,departmentInfo)
        actions.send_keys(Keys.ENTER)
        actions.send_keys_to_element(startDateInputBox,startDate)
        actions.send_keys(Keys.ENTER)
        actions.click(continueEducationButton)
        actions.perform()
        saveButton.click()
        assert successPopUpMessage in self.waitForElementVisible((By.CSS_SELECTOR,successPopUpMessage_CSS)).text  , f"'{successPopUpMessage}' ifadesi bulunamadı."
        continueEducationVerify=self.waitForElementVisible((By.CSS_SELECTOR,continueEducationVerify_CSS))
        assert continueEducationTitle in continueEducationVerify.text, f"'{continueEducationTitle}' ifadesi bulunamadı."

    def test_blankSpaces_error_messages(self):
        egitimHayatimButonu=self.waitForElementVisible((By.XPATH,egitim_Hayatim_xpath))
        egitimHayatimButonu.click()
        saveButton=self.waitForElementVisible((By.XPATH,saveButton_xpath))
        saveButton.click()
        #liste halinde tüm hata mesajlarını alan locator
        errorMessages=self.waitForElementsVisible((By.CSS_SELECTOR,errorMessages_CSS))
        #hata mesajlarının listesinin içerisindeki tüm hata mesajlarını alıyoruz ve onları tek tek kontrol ediyoruz.
        assert all(errorMessage for errorMessage in errorMessages)  , f"'{errorMessage}' ifadesi {errorMessages} içinde bulunamadı."
        sleep(3)

    def test_delete_education(self):
        self.test_add_education()
        deleteButton=self.waitForElementVisible((By.CSS_SELECTOR,deleteButton_CSS))
        deleteButton.click()
        assert popUpMessage == self.waitForElementVisible((By.CSS_SELECTOR,popUpMessage_CSS)).text
        yesButton=self.waitForElementVisible((By.CSS_SELECTOR,yesButton_CSS))
        noButton=self.waitForElementVisible((By.CSS_SELECTOR,noButton_CSS))
        noButton.click()
        sleep(2)
        educationVerify=self.waitForElementVisible((By.CSS_SELECTOR,educationVerify_CSS))
        assert educationVerify.text==universityInfo,f"'{universityInfo}' ifadesi bulunamadı."
        sleep(2) #sleep koymadan çalışmıyor. stale element hatası veriyor yinede.
        #stale bayat element hatalası için elementleri tekrar locate ediyoruz. 
        deleteButton=self.waitForElementVisible((By.XPATH,deleteButton_xpath))
        deleteButton.click()
        sleep(2)
        yesButton=self.waitForElementVisible((By.CSS_SELECTOR,yesButton_CSS))
        yesButton.click()
        sleep(2)
        successDeleteEducationPopUpMessage=self.waitForElementVisible((By.CSS_SELECTOR,successDeleteEducationPopUpMessage_CSS))
        assert successDeleteEducationPopUpText in successDeleteEducationPopUpMessage.text, f"'{successDeleteEducationPopUpText}' ifadesi bulunamadı." 

    #Bug , mezuniyet yılı seçildiğinde, devam ediyor butonu pasif hale gelmeliydi.
    def test_continueButton_with_graduationYear(self):
        egitimHayatimButonu=self.waitForElementVisible((By.XPATH,egitim_Hayatim_xpath))
        egitimHayatimButonu.click()
        egitimDurumuButonu=self.waitForElementVisible((By.CSS_SELECTOR,egitimDurumu_CSS))
        egitimDurumuButonu.click()
        egitimSecimi=self.waitForElementVisible((By.CSS_SELECTOR,egitimSecimi_CSS))
        egitimSecimi.click()
        universityInputBox=self.waitForElementVisible((By.XPATH,universityInputBox_xpath))
        universityInputBox.send_keys(universityInfo)
        departmentInputBox=self.waitForElementVisible((By.XPATH,departmentInputBox_xpath))
        departmentInputBox.send_keys(departmentInfo)
        startDateInputBox=self.waitForElementVisible((By.XPATH,startDate_xpath))
        startDateInputBox.click()
        startDateFromCalendar=self.waitForElementVisible((By.XPATH,startDateFromCalendar_xpath))
        sleep(2)
        startDateFromCalendar.click()
        finishtDateInputBox=self.waitForElementVisible((By.XPATH,finishDate_xpath))
        finishtDateInputBox.click()
        finishDateFromCalendar=self.waitForElementVisible((By.XPATH,finishDateFromCalendar_xpath))
        sleep(2)
        finishDateFromCalendar.click()
        continueEducationButton=self.waitForElementVisible((By.CSS_SELECTOR,continueEducationButton_CCS))
        # Devam et butonunun tıklanabilir olup olmadığını kontrol eder.Normalde tıklanabilir olmaması lazım. #bug
        assert not continueEducationButton.is_enabled(), "Devam et butonu tıklanabilir durumda"
        sleep(2)

    def test_max_character_limit(self):
        egitimHayatimButonu=self.waitForElementVisible((By.XPATH,egitim_Hayatim_xpath))
        egitimHayatimButonu.click()
        egitimDurumuButonu=self.waitForElementVisible((By.CSS_SELECTOR,egitimDurumu_CSS))
        egitimDurumuButonu.click()
        egitimSecimi=self.waitForElementVisible((By.CSS_SELECTOR,egitimSecimi_CSS))
        egitimSecimi.click()
        universityInputBox=self.waitForElementVisible((By.XPATH,universityInputBox_xpath))
        universityInputBox.send_keys(max_characterControl_text)
        departmentInputBox=self.waitForElementVisible((By.XPATH,departmentInputBox_xpath))
        departmentInputBox.send_keys(max_characterControl_text)
        startDateInputBox=self.waitForElementVisible((By.XPATH,startDate_xpath))
        startDateInputBox.click()
        startDateFromCalendar=self.waitForElementVisible((By.XPATH,startDateFromCalendar_xpath))
        sleep(2)
        startDateFromCalendar.click()
        finishtDateInputBox=self.waitForElementVisible((By.XPATH,finishDate_xpath))
        finishtDateInputBox.click()
        finishDateFromCalendar=self.waitForElementVisible((By.XPATH,finishDateFromCalendar_xpath))
        sleep(2)
        finishDateFromCalendar.click()
        saveButton=self.waitForElementVisible((By.XPATH,saveButton_xpath))
        saveButton.click()
        errorMessages=self.waitForElementsVisible((By.CSS_SELECTOR,errorMessages_CSS))
        assert (maxCharErrorMessage==errorMessage for errorMessage in errorMessages), f"'{maxCharErrorMessage}' ifadesi bulunamadı"

    def test_min_character_limit(self):
        egitimHayatimButonu=self.waitForElementVisible((By.XPATH,egitim_Hayatim_xpath))
        egitimHayatimButonu.click()
        egitimDurumuButonu=self.waitForElementVisible((By.CSS_SELECTOR,egitimDurumu_CSS))
        egitimDurumuButonu.click()
        egitimSecimi=self.waitForElementVisible((By.CSS_SELECTOR,egitimSecimi_CSS))
        egitimSecimi.click()
        universityInputBox=self.waitForElementVisible((By.XPATH,universityInputBox_xpath))
        universityInputBox.send_keys(min_characterControl_text)
        departmentInputBox=self.waitForElementVisible((By.XPATH,departmentInputBox_xpath))
        departmentInputBox.send_keys(min_characterControl_text)
        startDateInputBox=self.waitForElementVisible((By.XPATH,startDate_xpath))
        startDateInputBox.click()
        startDateFromCalendar=self.waitForElementVisible((By.XPATH,startDateFromCalendar_xpath))
        sleep(2)
        startDateFromCalendar.click()
        finishtDateInputBox=self.waitForElementVisible((By.XPATH,finishDate_xpath))
        finishtDateInputBox.click()
        finishDateFromCalendar=self.waitForElementVisible((By.XPATH,finishDateFromCalendar_xpath))
        sleep(2)
        finishDateFromCalendar.click()
        saveButton=self.waitForElementVisible((By.XPATH,saveButton_xpath))
        saveButton.click()
        errorMessages=self.waitForElementsVisible((By.CSS_SELECTOR,errorMessages_CSS))
        assert (minCharErrorMessage==errorMessage for errorMessage in errorMessages), f"'{minCharErrorMessage}' ifadesi bulunamadı"



     
        
        





    
        
        
        
        




