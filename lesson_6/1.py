from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://uitestingplayground.com/ajax")

driver.set_window_size(500, 400)
driver.implicitly_wait (30)

element = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, 'div [id=content]')
p = content.find_element(By.CSS_SELECTOR, 'p').text

print(p)
driver.quit()
