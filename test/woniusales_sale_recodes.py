import time
from selenium import webdriver
import pymysql


def connect_mysql():
    db = pymysql.connect("192.168.7.102", "root", "123456", "woniusales", charset="utf8")
    cur = db.cursor()
    cur.execute("select count(*) from sell")
    data = cur.fetchone()[0]
    cur.close()
    db.close()
    return data


driver = webdriver.Chrome()
driver.get("http://192.168.7.102:8080/woniusales/")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("Milor123")
driver.find_element_by_id("verifycode").send_keys("0000")
driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
time.sleep(2)
if driver.find_element_by_link_text("注销"):
    print("登录成功")
else:
    print("登录失败")
if "管理员" in driver.find_element_by_xpath("//*[@id=\"navbar\"]/ul[2]/li[1]/a").text:
    print("身份正确")
else:
    print("身份错误")
driver.find_element_by_link_text("销售报表").click()
r_count = connect_mysql()
print(r_count)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[1]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[2]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/button[3]").click()
time.sleep(1)
# 查找列表里记录的总数量
count = driver.find_elements_by_xpath("//*[@id=\"selldetail\"]/tbody/tr")
print(len(count))
if count == r_count:
    print("查询成功")
else:
    print("查询失败")
