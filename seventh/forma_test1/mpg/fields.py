from selenium.webdriver.common.by import By
from selenium import webdriver

class fields:

    def __init__(self, driver):
        #driver = webdriver.Firefox()
        self.driver = driver

    def check (self):
        self.class_first_neme = (By.ID, 'first-neme')
        self.class_last_neme = (By.ID, 'last-name')
        self.class_address = (By.ID, 'address')
        self.class_email = (By.ID, 'e-mail')
        self.class_phone = (By.ID, 'phone')
        self.class_zip_code = (By.ID, 'zip-code')
        self.class_city = (By.ID, 'city')
        self.class_country = (By.ID, 'country')
        self.class_job_position = (By.ID, 'job-position')
        self.class_compani = (By.ID, 'company')
        
    def get_class_fn(self):
        return self.driver.find_element(*self.class_first_neme).get_attribute("class")
    
    def get_class_ln(self):
        return self.driver.find_element(*self.class_last_neme).get_attribute("class")
    
    def get_class_addr(self):
        return self.driver.find_element(*self.class_address).get_attribute("class")
    
    def get_class_email(self):
        return self.driver.find_element(*self.class_email).get_attribute("class")
    
    def get_class_ph(self):
        return self.driver.find_element(*self.class_phone).get_attribute("class")
    
    def get_class_zip(self):
        return self.driver.find_element(*self.class_zip_code).get_attribute("class")
    
    def get_class_city(self):
        return self.driver.find_element(*self.class_city).get_attribute("class")
    
    def get_class_coun(self):
        return self.driver.find_element(*self.class_country).get_attribute("class")
    
    def get_class_job(self):
        return self.driver.find_element(*self.class_job_position).get_attribute("class")
    
    def get_class_comp(self):
        return self.driver.find_element(*self.class_compani).get_attribute("class")