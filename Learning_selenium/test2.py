from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x1, x2):
    return str(int(x1)+int(x2))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element_1 = browser.find_element_by_css_selector("#num1")
    x_value_1 = x_element_1.text
    print("x1= ", x_value_1)
    x_element_2 = browser.find_element_by_css_selector("#num2")
    x_value_2 = x_element_2.text
    print("x2= ", x_value_2)
    y = calc(x_value_1, x_value_2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()