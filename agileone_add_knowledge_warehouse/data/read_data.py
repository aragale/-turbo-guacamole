import xlrd
from agileone_add_knowledge_warehouse.common.add_knowledge_warehouse import Add

# 实例化excel文件对象
excel = xlrd.open_workbook(r"case_data.xlsx")
# 获取excel文件的sheet1对象（下标从0开始）
sheet = excel.sheets()[0]

# 从第1行开始循环（下标从0开始）
# for i in range(sheet.nrows):
    # 从第一列开始循环
    # for j in range(sheet.ncols):
        # 打印第i行，第j列的单元格的值
        # print(sheet.cell(i, j).value, end="\t\t")
    # print("\n")

# 从第二行开始取值（标题栏内容不需要）
for i in range(1, sheet.nrows):
    # 取第i行的值
    all_values = sheet.row_values(i)
    # print(all_values)
    need_values = all_values[-1:-4:-1]
    print(need_values)

    Add(int(need_values[2]), need_values[1], need_values[0])
