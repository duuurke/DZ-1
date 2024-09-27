from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://uitestingplayground.com/textinput")

driver.set_window_size(800, 500)
driver.implicitly_wait (30)

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(txt)
driver.quit() 
