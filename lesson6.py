from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num = browser.find_element_by_id("treasure").get_attribute('valuex')
    browser.find_element_by_xpath('//*[@id="answer"]').send_keys(calc(num))
    browser.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
    browser.find_element_by_xpath('/html/body/div/form/div/div/button').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
