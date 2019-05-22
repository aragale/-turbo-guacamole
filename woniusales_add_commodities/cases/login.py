import time
from selenium import webdriver


def login():
    driver = webdriver.Chrome()
    driver.get("http://192.168.7.102:8080/woniusales/")
    driver.maximize_window()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("Milor123")
    driver.find_element_by_id("verifycode").send_keys("0000")
    driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
    time.sleep(1)


if __name__ == '__main__':
    login()
