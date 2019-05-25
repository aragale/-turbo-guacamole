import xlsxwriter
from notice_and_meeting.util import count_cases
import time


class WriteReport:
    def __init__(self):
        # 创建excel文件
        self.excel = xlsxwriter.Workbook("TC_report.xlsx")
        # 在excel文件中创建sheet（页）
        self.report_sheet = self.excel.add_worksheet("agileone公告-会议模块测试报告")

    def set_sheet(self):
        # 根据A，B，C...设置列
        # 设置第一列宽度为15
        self.report_sheet.set_column("A:A", 15)
        # 设置第2列到第6列宽度为20
        self.report_sheet.set_column("B:F", 20)

        # 根据1，2，3...设置行（下标从0开始，即0表示第一行，excel文件中显示为1）
        # 设置第2行到第6行的高度为30磅
        # set_row()该方法只能逐行设置行高
        self.report_sheet.set_row(1, 30)
        self.report_sheet.set_row(2, 30)
        self.report_sheet.set_row(3, 30)
        self.report_sheet.set_row(4, 30)
        self.report_sheet.set_row(5, 30)
        self.report_sheet.set_row(6, 30)

    def set_format(self):
        # 设置两种文本样式
        self.style1 = self.excel.add_format({"bold": True, "font": 18, "border": 1})
        self.style2 = self.excel.add_format({"bold": True, "font": 14, "border": 1})
        # 设置文字垂直居中
        self.style1.set_align("vcenter")
        self.style2.set_align("vcenter")
        # 设置文字水平居中
        self.style1.set_align("center")
        self.style2.set_align("center")
        # 设置背景颜色
        self.style1.set_bg_color("#70DB93")
        # 设置字体颜色
        self.style1.set_color("#FFFFFF")

    def set_data(self):
        # 填写需要合并的单元格的位置，并设置样式
        self.report_sheet.merge_range("A1:F1", "测试报告总概况", self.style1)
        self.report_sheet.merge_range("A2:F2", "测试概括", self.style2)
        self.report_sheet.merge_range("A3:A6", "项目图片", self.style2)
        self.report_sheet.merge_range("F4:F6", "", self.style2)

        # 为合并区域填写内容，并设置样式，通过字母可以区分
        # 第二列
        self.report_sheet.write("B3", "项目名称", self.style2)
        self.report_sheet.write("B4", "系统版本", self.style2)
        self.report_sheet.write("B5", "运行环境", self.style2)
        self.report_sheet.write("B6", "测试网络", self.style2)
        # 第三列
        self.report_sheet.write("C3", "Agileone", self.style2)
        self.report_sheet.write("C4", "V1.4", self.style2)
        self.report_sheet.write("C5", "Windows10", self.style2)
        self.report_sheet.write("C6", "普通局域网", self.style2)
        # 第四列
        self.report_sheet.write("D3", "用例总数", self.style2)
        self.report_sheet.write("D4", "通过总数", self.style2)
        self.report_sheet.write("D5", "失败总数", self.style2)
        self.report_sheet.write("D6", "测试日期", self.style2)
        # 第五列
        self.report_sheet.write("E3", count_cases.fail_num+count_cases.pass_num, self.style2)
        self.report_sheet.write("E4", count_cases.pass_num, self.style2)
        self.report_sheet.write("E5", count_cases.fail_num, self.style2)
        self.report_sheet.write("E6", time.strftime("%Y-%m-%d %H:%M:%S"), self.style2)
        # 第六列
        self.report_sheet.write("F3", "分数", self.style2)
        # 关闭当前对excel的操作
        self.excel.close()

    def set_pie_chart(self):
        pie_chart = self.excel.add_chart({"type": "pie"})
        pie_chart.add_series({
            "name": "Agileone测试统计",
            "categories": "=测试总况!$D$4:$D$5",
            "values": "=测试总况!$E$4:$E$5",
        })
        pie_chart.set_title({"name": "Agileone测试统计"})
        self.report_sheet.insert_chart("A9", pie_chart)

    def set_cylindrical_diagram(self):
        cylindrical_diagram = self.excel.add_chart({"type": "column"})
        cylindrical_diagram.add_series({
            "name": "用例执行结果",
            # 饼图右侧说明“通过用例数”，“失败用例数”
            "categories": "=测试总况!$D$4:$D$5",
            # 饼图显示的数据
            "values": "=测试总况!$E$4:$E$5",
        })
        cylindrical_diagram.set_title({"name": "Agileone测试统计"})
        cylindrical_diagram.set_y_axis({"name": "数量"})
        cylindrical_diagram.set_x_axis({"name": "结果分类"})
        self.report_sheet.insert_chart("A25", cylindrical_diagram)
        # 关闭文件对象
        self.excel.close()


if __name__ == "__main__":
    wr = WriteReport()
    wr.set_sheet()
    wr.set_format()
    wr.set_data()
    wr.set_cylindrical_diagram()
    wr.set_pie_chart()
