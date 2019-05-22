import time
import logging
from selenium import webdriver

log = logging.getLogger(__name__)

class BaseFunc:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/agileone")
        self.driver.implicitly_wait(2)

    def login(self):
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_id("login").click()

    def add_notice(self, headline, content):
        self.headline = headline
        self.content = content
        self.driver.find_element_by_partial_link_text("公告管理").click()
        self.driver.find_element_by_id("headline").send_keys(headline)
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("ke-iframe"))
        self.driver.find_element_by_xpath("/html/body").send_keys(content)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("add").click()

    def check_msg(self):
        time.sleep(1)
        msg = self.driver.find_element_by_id("msg").text
        log.info(msg)
        if "成功" in msg:
            log.info("新增[标题为：%s，内容为：%s] 公告成功" % (self.headline, self.content))
        else:
            log.info("新增[标题为：%s，内容为：%s] 公告失败" % (self.headline, self.content))

    def __del__(self):
        self.driver.close()
        # self.driver.quit()


if __name__ == '__main__':
    b = BaseFunc()
    b.login()
    b.add_notice("this is a test", "this is a test of adding notice")
    b.check_msg()
