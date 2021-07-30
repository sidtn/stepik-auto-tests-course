import os
from selenium import webdriver
import time
import math


def num_x(x):
    return str(math.log(abs(12*math.sin(int(x)))))


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_xpath('/html/body/form/div/div/button').click()
    browser.switch_to.alert.accept()
    num = int(browser.find_element_by_xpath('//*[@id="input_value"]').text)
    browser.find_element_by_xpath('//*[@id="answer"]').send_keys(num_x(num))
    browser.find_element_by_xpath('/html/body/form/div/div/button').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()