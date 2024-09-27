from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

dod = WebDriverWait(driver, 40)

dod.until(EC.presence_of_all_elements_located ((By.CSS_SELECTOR, '#award')))


str = driver.find_element(By.CSS_SELECTOR, 'img').get_attribute('srt')

print(str)
driver.quit() 
