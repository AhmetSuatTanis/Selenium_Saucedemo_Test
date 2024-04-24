import pytest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from constants.chatBotConstants import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import keyboard

class Test_ChatBot:
  def setup_method(self):
      self.driver=webdriver.Chrome()
      self.driver.maximize_window()
      self.driver.get(giris_URL)
  
  def teardown_method(self, method):
    self.driver.quit()

  def waitForElementVisible(self,locator,timeout=15):
      return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
  
  def waitForElementAvailableForIFrame(self,locator,timeout=10):
      return WebDriverWait(self.driver, timeout).until(ec.frame_to_be_available_and_switch_to_it(locator))
  
  def test_chatBot_communication(self):
    self.waitForElementAvailableForIFrame((By.XPATH,chatBot_Iframe_xpath))
    self.waitForElementVisible((By.XPATH, chatBot_xpath)).click()
    self.driver.switch_to.default_content()
    self.waitForElementAvailableForIFrame((By.XPATH,chatBotMessageBox_Iframe_xpath))
    messageBox=self.waitForElementVisible((By.XPATH,messageInputBox_xpath))
    messageBox.send_keys(messageText)
    sendButton=self.waitForElementVisible((By.XPATH,messageSendButton_xpath))
    sendButton.click()
    assert self.waitForElementVisible((By.XPATH,actualTitleOfMessageBox_xpath )).text==expectedTitleOfMessageBox
    assert expectedWelcomeMessage in self.waitForElementVisible((By.XPATH,actualWelcomeMessage_xpath)).text
    self.waitForElementVisible((By.XPATH,nameInputBox_xpath)).send_keys(name)
    self.waitForElementVisible((By.CSS_SELECTOR,nameSendButton_CSS)).click()
    #Normalde "Ahmet Suat" yazdığım için bana Memnun oldum Ahmet yazması gerekirken. ilk girdiğim "Selam" yazısı ile bana Memnun oldum Selam diyor.
    #Selam yazısını adım gibi alıp kullanıyor. Bug var burada
    assert expectedGreetingMessage in self.waitForElementVisible((By.XPATH,actualGreetingMessage_xpath)).text
    topicSelection=self.waitForElementVisible((By.XPATH,topicSelection_xpath))
    topicSelection.click()
    assert expectedSelectionMessage in self.waitForElementVisible((By.XPATH,actualSelectionMessage_xpath)).text
    topicSelection2=self.waitForElementVisible((By.XPATH,topicSelection2_xpath))
    topicSelection2.click()
    assert expectedEducationsMessage in self.waitForElementVisible((By.XPATH,actualEducationsMessage_xpath)).text
    topicSelection3=self.waitForElementVisible((By.XPATH,topicSelection3_xpath))
    topicSelection3.click()
    expectedEducations=["Dijital Gelişim","Profesyonel Gelişim","Yönetsel Gelişim"]
    #Bu kod, egitimler listesindeki her bir öğeyi self.waitForElementVisible(...).text stringinde arar. Tüm öğeler bulunursa True döner, aksi halde False döner. all fonksiyonu ise bu sonuçları birleştirir ve eğer tüm öğeler bulunursa True, aksi halde False döner.
    assert all(education in self.waitForElementVisible((By.XPATH,actualEducationsList_xpath)).text for education in expectedEducations)
    assert expectedHelpMessage == self.waitForElementVisible((By.XPATH,actualHelpMessage_xpath)).text
    yesButton=self.waitForElementVisible((By.XPATH,yesButton_xpath))
    noButton=self.waitForElementVisible((By.XPATH,noButton_xpath))
    noButton.click()
    lastResponseMessage=self.waitForElementVisible((By.XPATH,actualLastResponseMessage_xpath))
    assert expectedLastResponseMessage in lastResponseMessage.text
    #chatbotun kapatılması kısmı dahil değil şu anda 
    # minimizeButton=self.waitForElementVisible((By.CSS_SELECTOR,minimizeButton_CSS))
    # minimizeButton.click()
    # sleep(2)
    # #mesajlaşma içindeydik , default ana iframe e geri dönüş yapıyoruz.
    # self.driver.switch_to.default_content()
    # #Tekrar chat botu açmak için ana iframe içine inip tekrar chat bot iframe'mini seçiyoruz.
    # self.waitForElementAvailableForIFrame((By.XPATH,chatBot_Iframe_xpath))
    # self.waitForElementVisible((By.XPATH, chatBot_xpath)).click()
    # #chat bot kısmından ana default iframe içine geri dönüyoruz.
    # self.driver.switch_to.default_content()
    # #default iframe den mesajlaşma iframe ine giriş yapıyoruz.
    # self.waitForElementAvailableForIFrame((By.XPATH,chatBotMessageBox_Iframe_xpath))
    # sleep(2)
    # self.waitForElementVisible((By.CSS_SELECTOR,closeButton_CSS)).click()
    # sleep(2)
    # self.waitForElementVisible((By.CSS_SELECTOR,noButton_CSS)).click()
    # sleep(2)
    # self.waitForElementVisible((By.CSS_SELECTOR,closeButton_CSS)).click()
    # sleep(2)
    # self.waitForElementVisible((By.CSS_SELECTOR,yesButton_CSS)).click()
    # sleep(3)
    # self.waitForElementVisible((By.CSS_SELECTOR,commentInputBox_CSS)).send_keys(commentMessage)
    # self.waitForElementVisible((By.CSS_SELECTOR,commentSendButton_CSS)).click()
    # sleep(5)
  
  def test_chatBot_closeButton(self):
    Test_ChatBot.test_chatBot_communication(self)
    sleep(2)
    self.waitForElementVisible((By.CSS_SELECTOR,closeButton_CSS)).click()
    sleep(2)
    self.waitForElementVisible((By.CSS_SELECTOR,noButton_CSS)).click()
    sleep(2)
    self.waitForElementVisible((By.CSS_SELECTOR,closeButton_CSS)).click()
    sleep(2)
    self.waitForElementVisible((By.CSS_SELECTOR,yesButton_CSS)).click()
    sleep(3)
    self.waitForElementVisible((By.CSS_SELECTOR,commentInputBox_CSS)).send_keys(commentMessage)
    self.waitForElementVisible((By.CSS_SELECTOR,commentSendButton_CSS)).click()
    sleep(5)

  def test_chatBot_minimizeButton(self):
    Test_ChatBot.test_chatBot_communication(self)
    minimizeButton=self.waitForElementVisible((By.CSS_SELECTOR,minimizeButton_CSS))
    minimizeButton.click()
    sleep(2)
    #mesajlaşma içindeydik , default ana iframe e geri dönüş yapıyoruz.
    self.driver.switch_to.default_content()
    #Tekrar chat botu açmak için ana iframe içine inip tekrar chat bot iframe'mini seçiyoruz.
    self.waitForElementAvailableForIFrame((By.XPATH,chatBot_Iframe_xpath))
    self.waitForElementVisible((By.XPATH, chatBot_xpath)).click()
    sleep(3)

  def test_chatBot_clickNo_WithCloseButton(self):
    Test_ChatBot.test_chatBot_communication(self)
    sleep(2)
    self.waitForElementVisible((By.CSS_SELECTOR,closeButton_CSS)).click()
    sleep(2)
    self.waitForElementVisible((By.CSS_SELECTOR,noButton_CSS)).click()
    lastResponseMessage=self.waitForElementVisible((By.XPATH,actualLastResponseMessage_xpath))
    assert expectedLastResponseMessage in lastResponseMessage.text
    sleep(2)
  
  def test_chatBot_sendFile(self):
    self.waitForElementAvailableForIFrame((By.XPATH,chatBot_Iframe_xpath))
    self.waitForElementVisible((By.XPATH, chatBot_xpath)).click()
    self.driver.switch_to.default_content()
    self.waitForElementAvailableForIFrame((By.XPATH,chatBotMessageBox_Iframe_xpath))
    messageBox=self.waitForElementVisible((By.XPATH,messageInputBox_xpath))
    messageBox.send_keys(messageText)
    sendButton=self.waitForElementVisible((By.XPATH,messageSendButton_xpath))
    sendButton.click()
    assert self.waitForElementVisible((By.XPATH,actualTitleOfMessageBox_xpath )).text==expectedTitleOfMessageBox
    assert expectedWelcomeMessage in self.waitForElementVisible((By.XPATH,actualWelcomeMessage_xpath)).text
    self.waitForElementVisible((By.XPATH,nameInputBox_xpath)).send_keys(name)
    self.waitForElementVisible((By.CSS_SELECTOR,nameSendButton_CSS)).click()
    assert expectedGreetingMessage in self.waitForElementVisible((By.XPATH,actualGreetingMessage_xpath)).text
    addFileButton=self.waitForElementVisible((By.CSS_SELECTOR,addFileButton_CSS))
    addFileButton.click()
    sleep(3)
    chooseFileButton=self.waitForElementVisible((By.CSS_SELECTOR,chooseFileButton_CSS))
    chooseFileButton.click()
    sleep(3)
    #pc den dosya yüklemek için "import keyboard" modülünü ekledim ve eklemek istediğim dosyamın path'ini kopyalayıp
    #önüne "r" koyarak "keyboard.write()" metoduyla çıkan dosya gezgini arama kutusuna yazdım ve enter tuşuna tıkladım. 
    keyboard.write(r"C:\Users\AHMET\Desktop\SendFile\Yazlm_Kalite_ve_Test_Egitim_Mufredat.pdf")
    sleep(3)
    keyboard.press("enter")
    sleep(3)
    sendButtonForFile=self.waitForElementVisible((By.CSS_SELECTOR,sendButtonForFile_CSS))
    sendButtonForFile.click()
    uploadedFileName=self.waitForElementVisible((By.LINK_TEXT,"Yazlm_Kalite_ve_Test_Egitim_Mufredat.pdf"))
    #yüklediğim file gerçekten yüklendimi diye verify ettim.
    assert uploadedFileName.text=="Yazlm_Kalite_ve_Test_Egitim_Mufredat.pdf"
    sleep(3)
    



     
    

    
    
    
    

  
      
      






    








    
  
