from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_7.url_123 import calculator_url


class TY():

    def __init__(self, driver):
        #driver = webdriver.Firefox()
        self.driver = driver
        self.driver.get (calculator_url)
        

    def calculator(self):#изменить значение на "5"
        pole = self.driver.find_element(By.ID, "delay")
        pole.clear()
        pole.send_keys('1')

    def fill (self):#ввести данные в кадькулятор и нажать кнопку равно '='
        self.driver.find_element(By.XPATH, "//span[text() = '7']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '+']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '8']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '=']").click()

    def click_but(self):#убедиться что число равно "15"
        WebDriverWait(self.driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), '15'))
        return self.driver.find_element(By.CLASS_NAME, "screen").text
