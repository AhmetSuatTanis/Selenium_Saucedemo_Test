from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Test_SauceDemo:

    # def all_setting(self):
    #     driver=webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.get("https://www.saucedemo.com/")
    #     return driver.close
        
    """ def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/") """

    def test_blank_login(self):
        sleep(2)
        driver=self.all_setting()
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        userNameInput.send_keys("")
        passwordInput.clear()
        loginButton.click()
        sleep(2)
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage.text)
        testResult=errorMessage.text=="Epic sadface: Username is required"
        print(f"Test Sonucu: {testResult}")
    
    def test_blank_password_login(self):
        sleep(2)
        driver=self.all_setting()
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        userNameInput.send_keys("İrem Balci")
        sleep(1)
        passwordInput.clear()
        loginButton.click()
        sleep(1) 
        errorMessage=driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']")
        print(errorMessage.text)
        testResult=errorMessage.text=="Epic sadface: Password is required"
        print(f"Test Sonucu: {testResult}")
        passwordInput.clear()
        userNameInput.clear()

    def test_lockedUser_login(self):
        sleep(2)
        driver=self.all_setting()
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        userNameInput.send_keys("locked_out_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        sleep(1) 
        errorMessage=driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']")
        print(errorMessage.text)
        testResult=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu: {testResult}")
        sleep(2)
        passwordInput.clear()
        userNameInput.clear()

    def test_valid_login(self):
        sleep(2)
        driver=self.all_setting()
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        userNameInput.send_keys("standard_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        sleep(2) 
        listOfProducts=driver.find_elements(By.CSS_SELECTOR,"div[class='inventory_item']")
        print(len(listOfProducts))
        testResult=len(listOfProducts)==6
        print(f"Test Sonucu: {testResult}")

 
testClass=Test_SauceDemo()
testClass.test_blank_login()
sleep(2)
testClass.test_blank_password_login()
sleep(2)
testClass.test_lockedUser_login()
sleep(2)
testClass.test_valid_login()
sleep(2)




    

        




