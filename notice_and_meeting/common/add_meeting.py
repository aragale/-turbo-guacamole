import time


class AddMeeting:
    # def __init__(self, driver, organizer, address, topic, attendee, content):
    #     # self.driver = login()
    #     # time.sleep(1)
    #     self.driver = driver
    #     self.add_meeting(organizer, address, topic, attendee, content)
    #     self.judge(organizer, address, topic, attendee, content)
        # time.sleep(3)
        # self.driver.quit()

    def add_meeting(self, driver, organizer, address, topic, attendee, content):
        self.driver = driver
        time.sleep(1)
        self.driver.find_element_by_partial_link_text("会议记录").click()
        time.sleep(1)
        self.driver.find_element_by_id("organizer").send_keys(organizer)
        self.driver.find_element_by_xpath("//*[@id=\"venue\"]").send_keys(address)
        self.driver.find_element_by_id("topic").send_keys(topic)
        self.driver.find_element_by_id("attendee").send_keys(attendee)
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("ke-iframe"))
        self.driver.find_element_by_xpath("/html/body").send_keys(content)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("add").click()
        time.sleep(1)
        self.judge(organizer, address, topic, attendee, content)

    def judge(self, organizer, address, topic, attendee, content):
        msg = self.driver.find_element_by_id("msg").text
        exe_time = time.strftime("%Y-%m-%d %H:%M:%S")
        if "成功" in msg:
            info = "新增会议 主持人是：["+organizer + "，地点是："+address+"，议题是："+topic \
                   + "，参与人员是："+attendee+"内容是："+content+"] 成功 %s" % exe_time
            print(info)
            self.write_info(info)
        else:
            info = "新增会议 主持人是：[" + organizer + "，地点是：" + address + "，议题是：" + topic \
                   + "，参与人员是：" + attendee + "，内容是：" + content + "] 失败 %s" % exe_time
            print(info)
            self.write_info(info)

    def write_info(self, msg):
        with open(r"D:\project\python\GUI\notice_and_meeting\logs\log.txt", mode="a") as file:
            file.write(msg + "\n")

    # def __del__(self):
    #     self.driver.quit()


# if __name__ == "__main__":
#     AddMeeting("test", "1", "2", "3", "this is a test!")
