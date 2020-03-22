from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element_by_css_selector("#book")
button.click()
browser.execute_script("window.scrollBy(0, 500);")
x_value = browser.find_element_by_css_selector("#input_value")
result = calc(x_value.text)
res_text = browser.find_element_by_css_selector("#answer")
res_text.send_keys(result)
but2 = browser.find_element_by_css_selector("#solve")
but2.click()

time.sleep(20)
browser.quit()
