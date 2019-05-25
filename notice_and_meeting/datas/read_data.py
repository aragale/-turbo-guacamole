import sys
import xlrd
from notice_and_meeting.common.login import login
from notice_and_meeting.util import count_cases

excel = xlrd.open_workbook("case_data.xlsx")
sheet = excel.sheets()[0]
# login()
driver = login()


for i in range(1, sheet.nrows):
# for i in range(5, sheet.nrows):
    all_values = sheet.row_values(i)
    log_values = "用例标题："+all_values[1] + "  预期结果："+all_values[12]
    # notice_values = all_values[]
    # meeting_values = all_values[]
    # 动态导包
    __import__("notice_and_meeting.common." + all_values[2])
    # 加载内存
    m = sys.modules["notice_and_meeting.common." + all_values[2]]
    # print(m)
    # 根据模块名找类名
    cname = getattr(m, all_values[3])
    # print(cname)
    # 根据（类的实例化）对象找方法
    # method = getattr(cname(), all_values[4])
    if "AddNotice" in str(cname):
        method = getattr(cname(), all_values[4])
        method(driver, all_values[5], all_values[6], log_values)
    elif "AddMeeting" in str(cname):
        method = getattr(cname(), all_values[4])
        method(driver, all_values[7], all_values[8], all_values[9], all_values[10], all_values[11], log_values)
        # method(organizer=all_values[7], address=all_values[8], topic=all_values[9], attendee=all_values[10],
        #        content=all_values[11])

print(count_cases.pass_num)
print(count_cases.fail_num)

driver.quit()
