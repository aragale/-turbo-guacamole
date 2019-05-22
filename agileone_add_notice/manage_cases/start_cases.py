import os
import glob

case_list = glob.glob(r"D:\project\python\GUI\agileone_add_notice\cases\case*.py")
# print(case_list)
try:
    for file in case_list:
        command = "python %s 1 >> ../logs/log.%d.txt 2>&1" % file
        os.system(command)
        # pass
except Exception as e:
    print(e)
