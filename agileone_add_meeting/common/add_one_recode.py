import time
# from agileone_add_meeting.common.login import start_chrome
from agileone_add_meeting.common.login import login


class InsertRecord:
    def __init__(self, organizer, address, topic, attendee, content):
        self.driver = login()
        # time.sleep(2)
        # self.driver = start_chrome()
        self.organizer = organizer
        self.address = address
        self.topic = topic
        self.attendee = attendee
        self.content = content
        time.sleep(1)
        self.driver.find_element_by_partial_link_text("会议记录").click()
        time.sleep(1)
        self.insert_record()
        self.judge()

    def insert_record(self):
        self.driver.find_element_by_id("organizer").send_keys(self.organizer)
        self.driver.find_element_by_xpath("//*[@id=\"venue\"]").send_keys(self.address)
        self.driver.find_element_by_id("topic").send_keys(self.topic)
        self.driver.find_element_by_id("attendee").send_keys(self.attendee)
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("ke-iframe"))
        self.driver.find_element_by_xpath("/html/body").send_keys(self.content)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("add").click()
        time.sleep(1)

    def judge(self):
        msg = self.driver.find_element_by_id("msg").text
        if "成功" in msg:
            info = "新增会议 主持人是："+self.organizer + "，地点是："+self.address+"，议题是："+self.topic \
                   + "，参与人员是："+self.attendee+"内容是："+self.content+" 成功"
            print(info)
            self.write_info(info)
        else:
            info = "新增会议 主持人是：" + self.organizer + "，地点是：" + self.address + "，议题是：" + self.topic \
                   + "，参与人员是：" + self.attendee + "，内容是：" + self.content + " 失败"
            print(info)
            self.write_info(info)

    def write_info(self, msg):
        with open(r"D:\project\python\GUI\agileone_add_meeting\logs\log.txt", mode="a") as file:
            file.write(msg + "\n")

    def __del__(self):
        self.driver.quit()
