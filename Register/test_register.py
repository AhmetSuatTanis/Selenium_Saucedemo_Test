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


class Test_Register:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Register_URL) #constants klasörü açarak içine değişkenler oluşturduk ordan çektik

    def teardown_method(self):
        self.driver.quit()
    
    
    def test_valid_register(self):
        userNameInput=self.waitForElementVisible((By.NAME,username_name))
        userLastNameInput=self.waitForElementVisible((By.NAME,userLastName_name))
        userEmailInput=self.waitForElementVisible((By.NAME,userEmail_name))
        userPasswordInput=self.waitForElementVisible((By.NAME,userPassword_name))
        userPasswordAgainInput=self.waitForElementVisible((By.NAME,userPasswordAgain_name))
        registerButton=self.waitForElementVisible((By.CSS_SELECTOR,registerButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(userLastNameInput,userLastname)
        actions.send_keys_to_element(userEmailInput,userEmail)
        actions.send_keys_to_element(userPasswordInput,userPassword)
        actions.send_keys_to_element(userPasswordAgainInput,userPassword)
        actions.click(registerButton)
        actions.perform()
        agreement1=self.waitForElementVisible((By.NAME,agreement1_name))
        agreement1.click()
        agreement2=self.waitForElementVisible((By.NAME,agreement2_name))
        agreement2.click()
        agreement3=self.waitForElementVisible((By.NAME,agreement3_name))
        agreement3.click()
        agreement4=self.waitForElementVisible((By.NAME,agreement4_name))
        agreement4.click()
        phoneNumberInput=self.waitForElementVisible((By.ID,phoneNumberInput_id))
        phoneNumberInput.send_keys(userPhoneNumber)
        self.waitForElementAvailableForIFrame((By.XPATH,reCAPTHCHA_iframe_xpath))
        reCAPTHCHA=self.waitForElementClickable((By.CLASS_NAME, "recaptcha-checkbox-border"))
        reCAPTHCHA.click()
        #WebDriverWait(self.driver, 10).until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]")))
        # WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border"))).click()
        self.driver.switch_to.default_content()
        sleep(15) #reCAPTHCHA için elle müdahele süresi
        continueButton=self.waitForElementVisible((By.CSS_SELECTOR,continueButton_CSS))
        continueButton.click()
        successRegisterMessage=self.waitForElementVisible((By.CSS_SELECTOR,successRegisterMessage_CSS))
        successRegisterMessage_text=successRegisterMessage.text
        expected_text="Tobeto Platform'a kaydınız başarıyla gerçekleşti."
        assert expected_text in successRegisterMessage_text, f"'{expected_text}' ifadesi mesaj içinde bulunamadı."
        #tek satıra indirmeyi dene   expected_message==suc

    
    
    def readInvalidDataFromExcel():
        excelFile = openpyxl.load_workbook("data/bosBirakilanYerler.xlsx") #dosyanın nerde olduğunu gösterdik data klasöründe 
        sheet = excelFile["sheet1"] #sayfa değişkeni oluşturduk ve sayfayı söyledik
        rows = sheet.max_row #kaçıncı satıra kadar verim var onu söyledik
        data = []
        for i in range(2,rows): #parametreler 2.satırda olddan 2den başlattık, veri 4te bitiyor ama rows +1 yazıyoruz sondaki de dahil olsun diye
            username = sheet.cell(i,1).value #satırın 1.hücresi username'e gitsin. hücrenin içindeki değere ulaşmak için .value yazdık
            userLastname = sheet.cell(i,2).value
            password = sheet.cell(i,3).value #satırın 2.hücresi password'e gitsin
            passwordAgain = sheet.cell(i,4).value
            email = sheet.cell(i,5).value

            username = "" if username is None else username
            userLastname = "" if userLastname is None else userLastname
            password = "" if password is None else password
            passwordAgain = "" if passwordAgain is None else passwordAgain
            email = "" if email is None else email

            data.append((username,userLastname,password,passwordAgain,email)) 
        return data  #kullanılan noktaya bu datayı göndermek istediğimizi söylüyoruz
    
    @pytest.mark.parametrize("username,userLastname,password,passwordAgain,email",readInvalidDataFromExcel())
    def test_invalid_register(self,username,userLastname,password,passwordAgain,email):
        userNameInput=self.waitForElementVisible((By.NAME,username_name))
        userLastNameInput=self.waitForElementVisible((By.NAME,userLastName_name))
        userEmailInput=self.waitForElementVisible((By.NAME,userEmail_name))
        userPasswordInput=self.waitForElementVisible((By.NAME,userPassword_name))
        userPasswordAgainInput=self.waitForElementVisible((By.NAME,userPasswordAgain_name))
        registerButton=self.waitForElementVisible((By.CSS_SELECTOR,registerButton_CSS))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(userLastNameInput,userLastname)
        actions.send_keys_to_element(userEmailInput,email)
        actions.send_keys_to_element(userPasswordInput,password)
        actions.send_keys_to_element(userPasswordAgainInput,passwordAgain)
        actions.perform()

        # Kayıt ol butonunun devre dışı olup olmadığını kontrol et
        #assert registerButton.get_attribute("disabled") == "true", "Kayıt ol butonu devre dışı değil."
        assert not registerButton.is_enabled(), "Kayıt ol butonu etkin durumda."



    def waitForElementVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementAvailableForIFrame(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.frame_to_be_available_and_switch_to_it((locator)))
    
    def waitForElementClickable(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((locator)))
    
 