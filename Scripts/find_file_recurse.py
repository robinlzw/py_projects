#!/usr/bin/env python
# -*- coding : utf-8 -*-
# coding: utf-8

import os
import sys
import time
import re

rmFileName = []
file_types = [".cpp", ".h"]


def usage():
    print('usage:%s --input=[value] --output=[value] ')
    sys.exit()


def listDir(fileDir, year, b_delete, to_find_str):
    for eachFile in os.listdir(fileDir):
        if os.path.isfile(fileDir + "/" + eachFile):  # 如果是文件，判断最后修改时间，符合条件进行删除
            ft = os.stat(fileDir + "/" + eachFile)
            ltime = time.localtime(int(ft.st_mtime))  # 获取文件最后修改时间
            file_year = time.strftime("%Y", ltime)

            if eachFile not in rmFileName:
                with open(fileDir + "/" + eachFile, 'r', encoding='utf8') as f:
                    foundLine = find_str_in_file(f, to_find_str)
                    if foundLine != "!!!???":
                        print("****" + foundLine + "####" + fileDir + "/" + eachFile)

                if b_delete:
                    print("删除文件: " + fileDir + "//" + eachFile)
                    # os.remove(fileDir + "/" + eachFile);  # 删除文件
            else:
                print("qrc:: " + eachFile)
        elif os.path.isdir(fileDir + "/" + eachFile):  # 如果是文件夹，继续递归
            listDir(fileDir + "/" + eachFile, year, b_delete, to_find_str)


def del_emp_dir(path):
    for root, dirs, files in os.walk(path):
        if not os.listdir(root):
            try:
                os.rmdir(root)
            except Exception as e:
                pass


def find_str_in_file(file, to_find_str):
    for line in file.readlines():
        # try:
        #     #             print(line)
        #     #             print(line.decode('utf8'))
        #     line.decode('utf8')
        #     # 为了暴露出错误，最好此处不print
        #
        # except:
        #     #print("to_find_str not in line")
        #     not_print_str = "not print"

        if to_find_str in line:
            print(line)
            file.close()
            return line

    file.close()
    return "!!!???"


def list_file_in_dir(input_dir, to_find_str):
    for root, dirs, files in os.walk(input_dir):
        for f in files:
            for fileType in file_types:
                if f.lower().endswith(fileType):
                    filename = os.path.join(root, f)
                    with open(filename) as my_file_handler:
                        try:
                            find_str_in_file(my_file_handler, to_find_str)
                        except Exception as e:
                            print(e)


if __name__ == '__main__':
    rootPath = "C:/Users/lenovo/source/git_work_space/slate"
    # openFileName = "E:\work\client_QML_final2\WindowsClient.qrc"

    # f = open(openFileName, "r")  # 设置文件对象
    # for rmFile in f.readlines():
    #     if "</file>" in rmFile:
    #         part1Item = rmFile.split('</')[0]
    #         fileItem = part1Item.rsplit('/', 1)[1]
    #         rmFileName.append(fileItem)
    #
    # f.close()  # 关闭文件

    # listDir(fileDir=rootPath, year=2019, b_delete=False, to_find_str="qt")
    list_file_in_dir(input_dir=rootPath, to_find_str="panelSplitView")
    # del_emp_dir(path)
