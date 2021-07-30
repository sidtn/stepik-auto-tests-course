import os
from selenium import webdriver
import time
import math


def num_x(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name('trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    num = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(num_x(num))
    browser.find_element_by_xpath('/html/body/form/div/div/button').click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()