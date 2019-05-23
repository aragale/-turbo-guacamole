import time
from selenium import webdriver


# def start_chrome():
#     driver = webdriver.Chrome()
#     driver.get("http://localhost/agileone/")
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     login()
#     return driver


def login():
    driver = webdriver.Chrome()
    driver.get("http://localhost/agileone/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    # driver = start_chrome()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("admin")
    driver.find_element_by_id("login").click()
    time.sleep(1)
    return driver


# if __name__ == '__main__':
#     login()
