import os
from selenium import webdriver
import time


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_xpath('/html/body/div/form/div/input[1]').send_keys('anat')
    browser.find_element_by_xpath('/html/body/div/form/div/input[2]').send_keys('piv')
    browser.find_element_by_xpath('/html/body/div/form/div/input[3]').send_keys('loh@gmail.com')
    browser.find_element_by_xpath('//*[@id="file"]').send_keys(file_path)
    browser.find_element_by_xpath('/html/body/div/form/button').click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()