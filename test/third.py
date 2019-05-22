import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("http://localhost/agileone")
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(2)

driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("admin")
driver.find_element_by_id("login").click()
driver.find_element_by_link_text("※ 公告管理 ※").click()

# 范围，下拉选择框，选择Agileone，下标为2（下标从0开始）
Select(driver.find_element_by_id("scope")).select_by_index(2)
driver.find_element_by_id("headline").send_keys("焦点切换")

# 焦点切换到frame内
# driver.switch_to.frame(driver.find_element_by_class_name("ke-iframe"))
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id=\"actionPanel\"]/tr[4]/td[2]/div/div/iframe"))
# 操作frame标签内的属性
driver.find_element_by_xpath("/html/body").send_keys("焦点切换到frame内")

# 焦点切换到当前页面
driver.switch_to.default_content()

driver.find_element_by_id("add").click()
time.sleep(2)
driver.close()
