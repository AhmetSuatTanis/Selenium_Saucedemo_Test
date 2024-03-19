from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com.tr/")
sleep(2)

input=driver.find_element(By.CLASS_NAME,"gLFyf")
input.send_keys("kodlama.io")
sleep(2)

searchButton=driver.find_element(By.CLASS_NAME,"gNO89b")
searchButton.click()
sleep(3)

button=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
button.click()
sleep(3)


listOfCourse=driver.find_elements(By.CLASS_NAME,"col-xs-12.col-sm-6.col-md-4")
print(f"Kodlama.io sitesinde {len(listOfCourse)} adet kurs vardir.")





