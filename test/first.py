import time
from selenium import webdriver
import pymysql


def connect_mysql():
    db = pymysql.connect("localhost", "root", "doremi", "agileone", charset="utf8")
    cur = db.cursor()
    cur.execute("select count(*) from notice")
    data = cur.fetchone()
    cur.close()
    db.close()
    return data


# 实例化Chromedirver对象（打开浏览器）
driver = webdriver.Chrome()
# driver.switchTo().defaultContent()
# 根据url打开网页
driver.get("http://localhost/agileone/")

# 隐式等待，设置一次，后面所有find_element_by_都会等待3秒
# driver.implicitly_wait(3)
time.sleep(2)
# 根据id查找元素，并将id=username的元素值设为“admin”
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("admin")
# 根据id查找按钮，并通过click()方法点击该按钮
driver.find_element_by_id("login").click()

# 强制等待，为了使代码运行速度慢一些，使页面元素出现后再执行下一步
time.sleep(2)
driver.find_element_by_link_text("※ 公告管理 ※").click()
# driver.find_element_by_xpath(r"/html/body/table/tbody/tr[2]/td[1]/div[1]/ul/li[1]/a").click()
time.sleep(1)
# num1 = eval(driver.find_element_by_id("totalRecord").text)
num1 = connect_mysql()[0]
# driver.find_element_by_id("noticeid").send_keys(100)
driver.find_element_by_id("headline").send_keys("hello, world!")

driver.find_element_by_xpath("//*[@id='actionPanel']/tr[4]/td[2]/div/table[1]/tbody/tr/td/table[1]/tbody/tr/td[1]/img").click()
driver.find_element_by_xpath("//*[@id='actionPanel']/tr[4]/td[2]/div/div/textarea").send_keys("hello, world!")
driver.find_element_by_id("add").click()
time.sleep(2)

# 根据提示信息做断言
# msg = driver.find_element_by_id("msg").text
# if "成功" in msg:
#     print("公告新增成功")
# else:
#     print("公告新增不成功")


# 根据公告列表中公告的数量做断言，点击新增前获取一次公告数量，点击新增后获取一次公告数量
# 比较获得的两次数量之差为1
# 页面设计：在左下角显示了总数
# num2 = eval(driver.find_element_by_id("totalRecord").text)
# if num2-num1 == 1:
#     print("公告新增成功")
# else:
#     print("公告新增不成功")

# 根据数据库查询做断言
num2 = connect_mysql()[0]
if num2-num1 == 1:
    print("公告新增成功")
else:
    print("公告新增不成功")

time.sleep(2)
# 关闭当前焦点所在的页面
driver.close()
