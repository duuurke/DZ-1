from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

Uname = driver.find_element(By.ID, 'username')
Uname.send_keys('Rneyp')
sleep(2)
Pword = driver.find_element(By.ID, 'password')
Pword.send_keys('12345')
sleep(2)
button = driver.find_element(By.TAG_NAME, 'button').click()
sleep(2)

driver.quit()

