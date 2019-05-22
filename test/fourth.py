import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("js注入")
# driver.find_element_by_id("su").click()
time.sleep(2)
# driver.find_element_by_link_text(" - ma_fighting - 博客园").click()
# 点击第一条搜索结果
ele = driver.find_element_by_xpath("//*[@id='1']/h3/a")
driver.execute_script("arguments[0].click();", ele)

# 获取第一个窗口的句柄
first_handle = driver.current_window_handle
# 获取由driver对象打开的所有窗口的句柄（此处只有两个）
all_handles = driver.window_handles
# 将焦点切换到最后打开的窗口
driver.switch_to.window(all_handles[-1])
time.sleep(1)
driver.find_element_by_id("q").send_keys("窗口切换")

# 将焦点切换回第一个窗口
driver.switch_to.window(first_handle)
# 清除搜索框中的内容
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("第二次切换")
