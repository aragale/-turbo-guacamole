import time
from selenium import webdriver
import pymysql


def connect_mysql():
    db = pymysql.connect("192.168.7.102", "root", "123456", "woniusales", charset="utf8")
    cur = db.cursor()
    cur.execute("select count(*) from customer")
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
num1 = connect_mysql()
time.sleep(1)
driver.find_element_by_link_text("会员管理").click()
time.sleep(2)
# driver.find_element_by_id("customerphone").send_keys("13240407675")
driver.find_element_by_id("customerphone").send_keys("13240407674")
driver.find_element_by_css_selector("body > div.container > div:nth-child(1) > form.form-inline "                                   
                                    "> div.col-lg-4.col-md-4.col-sm-4.col-xs-4 > button:nth-child(1)").click()

# 根据添加重复的会员号码，提示“”做断言
# time.sleep(1)
# driver.find_element_by_id("customerphone").send_keys("13240407675")
# driver.find_element_by_css_selector("body > div.container > div:nth-child(1) > form.form-inline >
# div.col-lg-4.col-md-4.col-sm-4.col-xs-4 > button:nth-child(1)").click()
# time.sleep(1)
# string = driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div").text
# if "重复添加" in string:
#     print("添加会员成功")
# else:
#     print("添加会员失败")

# 根据数据库查询会员数量做断言
time.sleep(1)
num2 = connect_mysql()
if num2-num1 == 1:
    print("添加会员成功")
else:
    print("添加会员失败")
# driver.find_element_by_css_selector("#customerlist > tr:nth-child(12) > td:nth-child(2)")
time.sleep(2)
driver.close()
