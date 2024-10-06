from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from time import sleep 


driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
driver.find_element(By.ID, 'shopping_cart_container').click()
driver.find_element(By.ID, 'checkout').click()
driver.find_element(By.ID, 'first-name').send_keys('инокентий')
driver.find_element(By.ID, 'last-name').send_keys('трактарин')
driver.find_element(By.ID, 'postal-code').send_keys('1489456')
driver.find_element(By.ID, 'continue').click()

p = driver.find_element(By.CLASS_NAME, 'summary_total_label')
total = p.text.strip().replace("total: $", '')

ex_total = '58.29'
assert total == ex_total 
print ('fитоговая сумма ${total}')
