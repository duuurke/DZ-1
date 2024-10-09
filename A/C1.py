from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from B1 import B1

def open_the_browser():
    driver = webdriver.Firefox()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    b1 = B1(driver)
    B1.gog()

def gog():
   b1.find_element(By.NAME, 'first-name').send_keys(First_name)

#B1.gtg()
  


    

# def test_2():
#     browzer = webdriver.Firefox()
#     browzer.get("")

# EC.presence_of_element_located
# counter = 0
# counter +=1

   



