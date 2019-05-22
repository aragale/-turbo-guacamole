import time

import uiautomation
# import subprocess
import os

# 通过subprocess打开记事本
# subprocess.Popen("notepad")

# 通过os.system打开记事本
os.system("start /b notepad")

# 获取记事本窗口对象
note_window = uiautomation.WindowControl(Name="无标题 - 记事本")

# 获取记事本编辑框窗口对象
edit = note_window.EditControl(AutomationId="15")
# note_window.EditControl(Name="文本编辑器")

# 点击元素，将光标放入元素中
# edit.Click()

# 向编辑框传入内容
edit.SendKeys("hello, world!")
time.sleep(1)

# 定位菜单栏中的“文件”
menu = note_window.MenuItemControl(Name="文件(F)")
menu.Click()

# 在“文件”菜单的子菜单中找到“保存”，点击
# save = uiautomation.MenuItemControl(Name="保存(S)")
# save.Click()

# 点击“文件”后，按三次“下”，在按一次“回车”，保存文件
# uiautomation.SendKey(uiautomation.Keys.VK_DOWN)
# uiautomation.SendKey(uiautomation.Keys.VK_DOWN)
# uiautomation.SendKey(uiautomation.Keys.VK_DOWN)
# uiautomation.SendKey(uiautomation.Keys.VK_ENTER)

# 利用快捷键保存文件内容，键入S
uiautomation.SendKey(uiautomation.Keys.VK_S)

# 由于在之前的操作完成后，光标自动进入文件名输入域
# 故，直接在新弹出的文件管理窗口，输入保存的文件路径和文件名
uiautomation.SendKeys(r"C:\Users\aragale\Desktop\demo.txt")

# 点击文件管理窗口的“保存”按钮
uiautomation.ButtonControl(Name="保存(S)").Click()

time.sleep(1)

# 检查文件是否存在
is_file = os.path.exists(r"C:\Users\aragale\Desktop\demo.txt")
# 或者
# is_file = os.path.isfile(r"C:\Users\aragale\Desktop\demo.txt")
if is_file:
    # 用os打开文件
    # os.system("start /b C:\\Users\\aragale\\Desktop\\demo.txt")
    # 读取文件内容
    # content = uiautomation.EditControl(AutomationId="15").GetValuePattern().Value

    # 文件读写
    with open(r"C:\Users\aragale\Desktop\demo.txt") as file:
        content = file.read()
    print(content)
    if content == "hello, world!":
        print("文件写入成功")
    else:
        print("文件写入失败")
else:
    print("文件不存在")

# 关闭记事本,直接用对象关闭
# note_window.Close()

# 用os关闭记事本
# os.system("taskkill /f /IM notepad")
