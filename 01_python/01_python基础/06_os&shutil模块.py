# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# author  Zhang Zhibang
import shutil

if __name__ == '__main__':
    # 1. os模块
    import os
    # 1.1调用操作系统命令
    # os.system("notepad.exe")
    # os.system("ping baidu.com")
    # 1.2文件目录
    d = './test'
    for file_name in os.listdir(d):
        new_file_name = file_name.replace("part","part-r-0000")
        print(new_file_name)
        shutil.move(d+"/"+file_name,d+"/"+new_file_name)
    print('done')
