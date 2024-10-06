from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from time import sleep 


driver = webdriver.Firefox()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

pole = driver.find_element(By.ID, 'delay')
pole.clear()
pole.send_keys('45')

driver.find_element(By.XPATH, "//span[text() = '7']").click()
driver.find_element(By.XPATH, "//span[text() = '+']").click()
driver.find_element(By.XPATH, "//span[text() = '8']").click()
driver.find_element(By.XPATH, "//span[text() = '=']").click()
sleep (1)

WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), '15'))
txt = driver.find_element(By.CLASS_NAME, "screen").text

def test():
 assert txt =='15'
sleep(5)

driver.quit()
