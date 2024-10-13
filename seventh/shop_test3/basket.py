from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_7.url_123 import shop_url

class basket():

    def __init__(self, driver):
        #driver = webdriver.Firefox()
        self.driver = driver
        self.driver.get (shop_url)
        

    def personal (self): #вход в систему+кликнуть кнопку логин
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
    def choose (self):#выбор товара + кликнуть кнопку корзину + ceckount
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
        self.driver.find_element(By.ID, 'shopping_cart_container').click()
    def data (self):#заполнить данные + кликнуть кнопкe continue
        self.driver.find_element(By.ID, 'checkout').click()
        self.driver.find_element(By.ID, 'first-name').send_keys('инокентий')
        self.driver.find_element(By.ID, 'last-name').send_keys('трактарист')
        self.driver.find_element(By.ID, 'postal-code').send_keys('1489456')
        self.driver.find_element(By.ID, 'continue').click()

    def price(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_all_elements_located ((By.CSS_SELECTOR,'.summary_total_label')))
        total = self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label')
        p = total.text.strip().replace("Total: $", '')

        return total