from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.degerlendirmelerConstants import *
#pre-conditions kısmı için giriş yapma, bilgiler ve locate pathleri için loginConstants import edildi.
from constants.loginConstants import *
from selenium.webdriver.common.keys import Keys

class Test_Degerlendirmeler:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(giris_URL)
        
    def pre_condition(self):
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

    def pre_condition1(self):
        emailInput=self.waitForElementVisible((By.CSS_SELECTOR,email_CSS))
        passwordInput=self.waitForElementVisible((By.CSS_SELECTOR,password_CSS))
        loginButton=self.waitForElementVisible((By.CSS_SELECTOR,loginButton_CSS))
        actions=ActionChains(self.driver)
        # actions.send_keys_to_element(emailInput,userEmail)
        # actions.send_keys_to_element(passwordInput,userPassword)
        #ilk test case çalışırken bu yorum satırını aktif et üstteki 2 satırı deaktif et !!!!
        actions.send_keys_to_element(emailInput,"vicihi7697@agafx.com")
        actions.send_keys_to_element(passwordInput,"Ahmet=12345")
        actions.click(loginButton)
        actions.perform()
        successPopupMessageClose=self.waitForElementVisible((By.CSS_SELECTOR,successPopupMessage_CSS))
        successPopupMessageClose.click()    
        

        
    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementsVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    #Bu test case her çalıştığında yeni bir profil maili vermemiz gerekmektedir.
    #Değerlendirme testinini çözme
    def test_solving_evaluations_test(self):
        self.pre_condition1()
        evaluationButton=self.waitForElementVisible((By.XPATH,evaluationButton_xpath))
        evaluationButton.click()
        tobetoTitle=self.waitForElementVisible((By.CSS_SELECTOR,tobetoTitleText_CSS))
        assert expectedTobetoTitle == tobetoTitle.text, f"'{expectedTobetoTitle}' ifadesi bulunamadı."
        startButton=self.waitForElementVisible((By.CSS_SELECTOR,startButton_CSS))
        startButton.click()
        assert isteBasariModeli_link1==self.driver.current_url
        startEvaluationButton=self.waitForElementVisible((By.CSS_SELECTOR,startEvaluationButton_CSS))
        actions = ActionChains(self.driver)
        actions.move_to_element(startEvaluationButton).perform()
        startEvaluationButton.click()
        assert isteBasariModeli_link2==self.driver.current_url
        #bu dış döngü 80 soru için 8 kere 10 ar adet sayfada çıkan soruyu cevaplar ve ileri tuşuna basarak sayfayı atlar.
        for _ in range(8):
            #bu iç döngü ise sorulara cevap vermek için xpath yolununu değiştirmek içindir
            #böylece her döngü sonunda i değeri artar ve 2. 3. 4. derken 10. soruya kadar bulup cevaplar.
            for i in range(1, 11):
                xpath = questionAnswers_xpath.format(i)
                questionAnswer=self.waitForElementVisible((By.XPATH,xpath))
                sleep(0.3)
                questionAnswer.click()
            #dış döngüden gelen sayı 7 olduğu zaman else girer ve finish tuşuna bastırır.    
            if _<7:
                forwardButton=self.waitForElementVisible((By.XPATH,forwardButton_xpath))
                actions.move_to_element(forwardButton).perform()
                forwardButton.click()
                sleep(1)
            else:
                finishButton=self.waitForElementVisible((By.XPATH,finishButton_xpath))
                actions.move_to_element(finishButton).perform()
                finishButton.click()
        
        sleep(2)
        actualMyAnalysisReport=self.waitForElementVisible((By.CSS_SELECTOR,actualMyAnalysisReport_CSS))
        assert expectedMyAnalysisReport==actualMyAnalysisReport.text, f"'{expectedMyAnalysisReport}' ifadesi bulunamadı."
        sleep(2)


    def test_display_of_evaluations(self):
        self.pre_condition()
        evaluationButton=self.waitForElementVisible((By.XPATH,evaluationButton_xpath))
        evaluationButton.click()
        sleep(2)
        showReport=self.waitForElementVisible((By.CSS_SELECTOR,showReport_CSS))
        showReport.click()
        sleep(2)
        assert expectedMyAnalysisReportLink==self.driver.current_url
        actualMyAnalysisReport=self.waitForElementVisible((By.CSS_SELECTOR,actualMyAnalysisReport_CSS))
        assert expectedMyAnalysisReport==actualMyAnalysisReport.text, f"'{expectedMyAnalysisReport}' ifadesi bulunamadı."
        sleep(2)

    def test_solving_test_of_software(self):
        self.pre_condition1()
        evaluationButton=self.waitForElementVisible((By.XPATH,evaluationButton_xpath))
        evaluationButton.click()
        sleep(2)
        frontEndStartButton=self.waitForElementVisible((By.XPATH,frontEndStartButton_xpath))
        frontEndStartButton.click()
        sleep(2)
        actualExamName=self.waitForElementVisible((By.CSS_SELECTOR,actualExamName_CSS))
        assert expectedExamName==actualExamName.text, f"'{expectedExamName}' ifadesi bulunamadı."
        startExamButton=self.waitForElementVisible((By.CSS_SELECTOR,startExamButton_CSS))
        startExamButton.click()
        for _ in range(25):
            firstOption=self.waitForElementVisible((By.XPATH,firstOption_xpath))
            firstOption.click()
            forwardQuestionButton=self.waitForElementVisible((By.XPATH,forwardQuestionButton_xpath))
            forwardQuestionButton.click()

        closeExamButton=self.waitForElementVisible((By.CSS_SELECTOR,closeExamButton_CSS))
        closeExamButton.click()
        sleep(2)
        frontEndShowReportButton=self.waitForElementVisible((By.XPATH,frontEndStartButton_xpath))
        frontEndShowReportButton.click()
        sleep(2)
        showReportButton=self.waitForElementVisible((By.CSS_SELECTOR,showReportButton_CSS))
        showReportButton.click()
        sleep(2)
        closeReportButton=self.waitForElementVisible((By.CSS_SELECTOR,closeReportButton_CSS))
        closeReportButton.click()
        sleep(2)


            







        



        


            
            
        