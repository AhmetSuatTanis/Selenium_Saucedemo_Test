from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait  #ilgili driverı bekleyen yapı
from selenium.webdriver.support import expected_conditions as ec  #
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_Demo:
    def deneme():
        print("deneme")

    #pytest tarafından tanımlanan method
    #bulunduğunda her test öncesi otomatik çalışır.
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    #her test bitiminde çalışacak fonksiyondur.
    def teardown_method(self):
        self.driver.quit

    #@pytest.mark.skip # tüm testler koşulurken "skip" şeklinde işaretlenen fonksiyonlarımı atla
    def test_demo(self):
        print("Merhaba")
        text="Hello"
        assert text=="Hello"
    
    def getData():
        return [("1","1"),("abc","123"),("deneme","secret_sauce")]

    
    # @pytest.mark.parametrize("username,password",[("1","1"),("abc","123"),("deneme","secret_sauce")])
    @pytest.mark.parametrize("username,password",getData())   #verileri başka kaynaktan alma kısmı.. getData()
    def test_invalid_login(self,username,password):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMesssage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMesssage.text=="Epic sadface: Username and password do not match any user in this service"

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()  #depoladığım aksiyonları çalıştır
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        baslik=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//div[@class='app_logo']")))
        assert baslik.text=="Swag Labs"
        

        