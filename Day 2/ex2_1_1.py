# 写代码实现文件复制功能：
# 需求描述：
# 用户输入拟复制的文件名称
# 若文件不存在，则报错。
# 用户输入新文件的名称
# 若新文件已经存在，则提示是否覆盖

import os

flag = '1'
file_name = input("please input the file name which you need copy").strip()
if not os.path.exists(file_name):
    print("the file does not exist")
    exit()

if os.path.exists(file_name):
    new_file = input("please input the new filename")
    if os.path.exists(new_file):
        print("overwrite?")
        flag = input("yes:input 1,no:input 0")
        if (flag == '0'):
            print("copy has stopped")

    else:
        if (flag == '1'):
            with open(file_name, "rb") as f_read:
                with open(new_file, "wb") as f_write:
                    while True:
                        data = f_read.read(102400)
                        if not data:
                            break
                        f_write.write(data)
        print("copy successfully")
