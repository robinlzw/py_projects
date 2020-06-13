#!/usr/bin/env python
# -*- coding : utf-8 -*-
# coding: utf-8

import os
import sys
import time
import re

rmFileName = []


def usage():
    print('usage:%s --input=[value] --output=[value] ')
    sys.exit()


def listDir(fileDir, year, b_delete, to_find_str):
    for eachFile in os.listdir(fileDir):
        if os.path.isfile(fileDir + "/" + eachFile):  # 如果是文件，判断最后修改时间，符合条件进行删除
            ft = os.stat(fileDir + "/" + eachFile)
            ltime = time.localtime(int(ft.st_mtime))  # 获取文件最后修改时间
            file_year = time.strftime("%Y", ltime)
            # if int(file_year) == int(year):

            if eachFile not in rmFileName:
                if "txt" in eachFile.rsplit('.', 1)[1]:
                    with open(fileDir + "/" + eachFile, 'r', encoding='utf8') as f:
                        find_str_in_file(f, to_find_str)
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
        # line = line.strip("\n")
        try:
            #             print(line)
            #             print(line.decode('utf8'))
            line.decode('utf8')
            # 为了暴露出错误，最好此处不print

        except:
            #print("to_find_str not in line")
            not_print_str = "not print"
        if to_find_str in line:
            if "展示文件" not in line:
                print("**************", line)
    file.close()


if __name__ == '__main__':
    # options, args = getopt.getopt(sys.argv[1:], '',['path=','year='])
    # for name, value in options:
    #     if name in ('-p','--path'):
    #         path = format(value)
    #     elif name in ('-y','--year'):
    #         year = format(value)
    #
    # if 'path' not in locals().keys() or not 'year' in locals().keys() :
    #     usage()
    rootPath = "E:/Documents"
    # openFileName = "E:\work\client_QML_final2\WindowsClient.qrc"

    # f = open(openFileName, "r")  # 设置文件对象
    # for rmFile in f.readlines():
    #     if "</file>" in rmFile:
    #         part1Item = rmFile.split('</')[0]
    #         fileItem = part1Item.rsplit('/', 1)[1]
    #         rmFileName.append(fileItem)
    #
    # f.close()  # 关闭文件
    # print(rmFileName)
    # listDir(fileDir="E:\work\client_QML_final2\Resources", year=2019)
    listDir(fileDir=rootPath, year=2019, b_delete=False, to_find_str="qt")
    # del_emp_dir(path)
