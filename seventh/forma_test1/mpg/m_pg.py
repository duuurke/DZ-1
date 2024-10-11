from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seventh.url_123 import forma_url
from seventh.forma_test1.data import *


class m_pg():

    def __init__(self, driver):
        #driver = webdriver.Firefox()
        self.driver = driver
        self.driver.get (forma_url)
    #заполнить данные изи фаила data, поле zip-code оставить пустым 
    def find_fields(self):
        self._first_neme = (By.NAME, 'first-name')
        self._last_name = (By.NAME, 'last-name')
        self._address = (By.NAME, 'address')
        self._email = (By.NAME, 'e-mail')
        self._phone = (By.NAME, 'phone')
        self._zip_code = (By.NAME, 'zip-code')
        self._city = (By.NAME, 'city')
        self._country = (By.NAME, 'country')
        self._job_position = (By.NAME, 'job-position')
        self._company = (By.NAME, 'company')
        self._button = (By.NAME, 'button')
    
    def filling_of_fields(self): #кликнуть по кнопке submit
        self.driver.find_element(*self._first_neme).send_keys(First_name)
        self.driver.find_element(*self._last_name).send_keys(Last_name)
        self.driver.find_element(*self._address).send_keys(Address)
        self.driver.find_element(*self._email).send_keys(Email)
        self.driver.find_element(*self._phone).send_keys(Phone_number)
        self.driver.find_element(*self._zip_code).send_keys(Zip_code)
        self.driver.find_element(*self._city).send_keys(City)
        self.driver.find_element(*self._country).send_keys(Country)
        self.driver.find_element(*self._job_position).send_keys(Job_position)
        self.driver.find_element(*self._company).send_keys(Company)

    def click_button(self):
        WebDriverWait (self.driver, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()