from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for _ in range (5):
    locator = 'button[onclick="addElement()"]'
    driver.find_element(By.CSS_SELECTOR, locator).click()
    sleep(1)

delete_locator = 'button.added-manually'#'button[onclick="deleteElement()"]'
se_isn = driver.find_elements(By.CSS_SELECTOR, delete_locator)

print(f'размер списка кнопоки delete в chrome: {len(se_isn)}')
