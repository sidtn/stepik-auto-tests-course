from selenium import webdriver
import math
import time

def num_x(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    num = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(num_x(num))
    browser.execute_script("window.scrollBy(0, 200);")
    browser.find_element_by_xpath('/html/body/div/form/div[2]/label').click()
    browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
    browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
    browser.find_element_by_xpath('/html/body/div/form/button').click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()