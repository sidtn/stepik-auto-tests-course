from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input').send_keys('Anaroli')
    browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input').send_keys('loh')
    browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input').send_keys('loh@gmail.com')
    browser.find_element_by_xpath('/html/body/div/form/button').click()


    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

