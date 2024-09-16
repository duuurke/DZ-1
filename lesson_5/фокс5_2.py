from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

close_modal = driver.find_element(By.TAG_NAME, 'input')
close_modal.send_keys('1000')
sleep(2)
close_modal.clear()
sleep(1)
close_modal.send_keys('999')
sleep(2)

driver.quit()
