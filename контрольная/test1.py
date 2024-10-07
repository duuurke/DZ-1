from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
 
def test_1():
    driver = webdriver.Firefox()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, 'first-name').send_keys(First_name)
    driver.find_element(By.NAME, 'last-name').send_keys(Last_name)
    driver.find_element(By.NAME, 'address').send_keys(Address)
    driver.find_element(By.NAME, 'e-mail').send_keys(Email)
    driver.find_element(By.NAME, 'phone').send_keys(Phone_number)
    driver.find_element(By.NAME, 'zip-code').send_keys(Zip_code)
    driver.find_element(By.NAME, 'city').send_keys(City)
    driver.find_element(By.NAME, 'country').send_keys(Country)
    driver.find_element(By.NAME, 'job-position').send_keys(Job_position)
    driver.find_element(By.NAME, 'company').send_keys(Company)

    WebDriverWait(driver, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()

    assert 'danger' in driver.find_element(By.ID, 'zip-code').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#first-name').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#last-name').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#address').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#e-mail').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#phone').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#city').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#country').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#job-position').get_attribute("class")
    assert 'success' in driver.find_element(By.ID, '#company').get_attribute("class")

    driver.quit()
