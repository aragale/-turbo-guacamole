import xlsxwriter


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
        self.report_sheet.write("C3", "", self.style2)
        self.report_sheet.write("C4", "", self.style2)
        self.report_sheet.write("C5", "", self.style2)
        self.report_sheet.write("C6", "", self.style2)
        # 第四列
        self.report_sheet.write("D3", "用例总数", self.style2)
        self.report_sheet.write("D4", "通过总数", self.style2)
        self.report_sheet.write("D5", "失败总数", self.style2)
        self.report_sheet.write("D6", "测试日期", self.style2)
        # 第五列
        self.report_sheet.write("E3", "", self.style2)
        self.report_sheet.write("E4", "", self.style2)
        self.report_sheet.write("E5", "", self.style2)
        self.report_sheet.write("E6", "", self.style2)
        # 第六列
        self.report_sheet.write("F3", "分数", self.style2)
        # 关闭当前对excel的操作
        self.excel.close()


if __name__ == "__main__":
    wr = WriteReport()
    wr.set_sheet()
    wr.set_format()
    wr.set_data()

