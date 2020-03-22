from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    x_text = browser.find_element_by_css_selector("#answer")
    x_text.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    browser.execute_script("window.scrollBy(0, 100);")
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()