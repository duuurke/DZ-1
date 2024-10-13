from seventh.calculator_test2.TY import TY
from selenium import webdriver

def test2():
    driver = webdriver.Firefox()
    calc = TY(driver)
    calc.calculator(1)
    calc.fill('7')
    calc.fill('+')
    calc.fill('8')
    calc.fill('=')
    assert "15" in calc.click_but()

    calc.driver.quit()
