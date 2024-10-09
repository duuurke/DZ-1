from lesson_7.calculator_test2.TY import TY
from selenium import webdriver

def test2():
    driver = webdriver.Firefox()
    calc = TY(driver)
    calc.calculator()
    calc.fill()
    
    assert "15" in calc.click_but()

    calc.driver.quit()
