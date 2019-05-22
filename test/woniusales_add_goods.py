import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://192.168.7.102:8080/woniusales/")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("Milor123")
driver.find_element_by_id("verifycode").send_keys("0000")
driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
time.sleep(1)
driver.find_element_by_link_text("商品入库").click()
time.sleep(1)
Select(driver.find_element_by_id("batchname")).select_by_index(0)
driver.find_element_by_id("goodsserial").send_keys("ME42404")
driver.find_element_by_id("barcode").send_keys("6955203636018")
driver.find_element_by_id("inputsize").send_keys("36-37-38-39")
driver.find_element_by_id("quantity").send_keys("3")
# driver.find_element_by_class_name("btn-primary form-control").click()
driver.find_element_by_xpath("/html/body/div[4]/div[1]/form[2]/div/input").click()
driver.switch_to.alert.accept()
msg = driver.find_element_by_id("message").text
if "失败" in msg:
    print("入库失败")
else:
    print("入库成功")
driver.save_screenshot("C:/Users/aragale/Desktop/add_goods.png")
