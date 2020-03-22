from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_name("firstname")
    name.send_keys("Vlad")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Medya")
    email = browser.find_element_by_name("email")
    email.send_keys("Vlad@gmail.com")
    path = os.path.abspath(os.path.dirname("__selenium.txt__"))    # PATH TO SPECIFIED FILE
    file_path = os.path.join(path, 'selenium.txt')                 # JOIN A NAME OF THE FILE
    print(path)
    file = browser.find_element_by_css_selector('#file').send_keys(path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()



