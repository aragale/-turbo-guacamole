from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost/agileone")
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("admin")
driver.find_element_by_id("login").click()
time.sleep(1)
driver.find_element_by_partial_link_text("公告管理").click()
# ele = driver.find_element_by_partial_link_text("公告管理")
time.sleep(1)
# webdriver.ActionChains(driver).context_click(ele).perform()
# ele.send_keys("T")
webdriver.ActionChains(driver).context_click(driver.find_element_by_xpath("//*[@id=\"actionPanel\"]/tr[4]/td[1]")).\
    send_keys(Keys.CONTROL, 'R').perform()
