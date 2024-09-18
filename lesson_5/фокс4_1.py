from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

btn = ("div.modal-footer > p")
Cmodal = driver.find_element(By.CSS_SELECTOR, btn)
sleep(3)

Cmodal.click()
sleep(2)
