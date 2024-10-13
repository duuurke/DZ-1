from seventh.forma_test1.mpg.fields import fields
from seventh.forma_test1.mpg.m_pg import m_pg
from selenium import webdriver

def test1():
    driver = webdriver.Firefox()
    mpg = m_pg(driver)
    mpg.find_fields()
    mpg.filling_of_fields()
    mpg.click_button()

    driver = webdriver.Firefox()
    fields (driver)
    fields.check()
    fields.get_class_fn()
    fields.get_class_ln()
    fields.get_class_addr()
    fields.get_class_email()
    fields.get_class_ph()
    fields.get_class_zip()
    fields.get_class_city()
    fields.get_class_coun()
    fields.get_class_job()
    fields.get_class_comp()

    assert "success" in fields.get_class_fn()
    assert "success" in fields.get_class_ln()
    assert "success" in fields.get_class_addr()
    assert "success" in fields.get_class_email()
    assert "success" in fields.get_class_ph()
    assert "danger" in fields.get_class_zip()
    assert "success" in fields.get_class_city()
    assert "success" in fields.get_class_coun()
    assert "success" in fields.get_class_job()
    assert "success" in fields.get_class_comp()
   
    driver.quit()
    