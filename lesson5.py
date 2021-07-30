from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num = browser.find_element_by_xpath('//*[@id="input_value"]').text
    browser.find_element_by_xpath('//*[@id="answer"]').send_keys(calc(num))
    browser.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    browser.find_element_by_xpath('/html/body/div/form/div[4]/label').click()
    browser.find_element_by_xpath('/html/body/div/form/button').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
