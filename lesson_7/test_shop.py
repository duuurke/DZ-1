from lesson_7.shop_test3.basket import basket
from selenium import webdriver

def test3():
    driver = webdriver.Firefox()
    calc = basket(driver)
    calc.personal()
    calc.choose()
    calc.data()
    calc.price()
    
    driver.quit()