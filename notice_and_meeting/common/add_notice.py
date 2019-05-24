import time
from notice_and_meeting.common.login import login


class AddNotice:
    def __init__(self, headline, content):
        self.driver = login()
        time.sleep(1)
        self.add_notice(headline, content)
        self.judge(headline, content)

    def add_notice(self, headline, content):
        self.driver.find_element_by_partial_link_text("公告管理").click()
        self.driver.find_element_by_id("headline").send_keys(headline)
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("ke-iframe"))
        self.driver.find_element_by_xpath("/html/body").send_keys(content)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("add").click()

    def judge(self, headline, content):
        time.sleep(1)
        msg = self.driver.find_element_by_id("msg").text
        print(msg)
        exe_time = time.strftime("%Y-%m-%d %H:%M:%S")
        if "成功" in msg:
            info = "新增 [标题为：%s，内容为：%s] 公告成功 %s" % (headline, content, exe_time)
            print(info)
            self.write_info(info)
        else:
            info = "新增 [标题为：%s，内容为：%s] 公告失败 %s" % (headline, content, exe_time)
            print(info)
            self.write_info(info)

    def write_info(self, info):
        with open(r"D:\project\python\GUI\notice_and_meeting\logs\log.txt", mode="a") as file:
            file.write(info + "\n")

    def __del__(self):
        self.driver.quit()


# if __name__ == "__main__":
#     AddNotice("test", "this is a test!")
