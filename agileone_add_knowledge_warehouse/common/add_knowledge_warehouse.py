import time
from selenium.webdriver.support.ui import Select
from agileone_add_knowledge_warehouse.common.login import login


class Add:
    def __init__(self, index, headline, content):
        self.driver = login()
        time.sleep(1)
        self.driver.find_element_by_partial_link_text("知识仓库").click()
        Select(self.driver.find_element_by_id("type")).select_by_index(index)
        self.driver.find_element_by_id("headline").send_keys(headline)
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("ke-iframe"))
        self.driver.find_element_by_xpath("/html/body").send_keys(content)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("add").click()
        time.sleep(1)
        self.judge()

    def judge(self):
        msg = self.driver.find_element_by_id("msg").text
        if "成功" in msg:
            print("知识仓库新增记录成功")
        else:
            print("知识仓库新增记录失败")

    def __del__(self):
        self.driver.quit()
