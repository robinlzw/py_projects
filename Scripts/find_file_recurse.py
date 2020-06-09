#!/usr/bin/env python
# coding: utf-8
import os
import sys
import time

rmFileName = []

def usage():
    print('usage:%s --input=[value] --output=[value] ')
    sys.exit()


def listDir(fileDir, year):
    for eachFile in os.listdir(fileDir):
        if os.path.isfile(fileDir + "/" + eachFile):  # 如果是文件，判断最后修改时间，符合条件进行删除
            ft = os.stat(fileDir + "/" + eachFile)
            ltime = time.localtime(int(ft.st_mtime))  # 获取文件最后修改时间
            file_year = time.strftime("%Y", ltime)
            #if int(file_year) == int(year):
            if eachFile not in rmFileName:
                print("删除文件: " + fileDir + "\\" + eachFile)
                os.remove(fileDir+"/"+eachFile);   #删除文件
            else:
                print("qrc:: " + eachFile)
        elif os.path.isdir(fileDir + "/" + eachFile):  # 如果是文件夹，继续递归
            listDir(fileDir + "/" + eachFile, year)


def del_emp_dir(path):
    for root, dirs, files in os.walk(path):
        if not os.listdir(root):
            try:
                os.rmdir(root)
            except Exception as e:
                pass


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

    f = open("E:\work\client_QML_final2\WindowsClient.qrc", "r")  # 设置文件对象
    for rmFile in f.readlines():
        if "</file>" in rmFile:
            part1Item = rmFile.split('</')[0]
            fileItem = part1Item.rsplit('/', 1)[1]
            rmFileName.append(fileItem)
            #print(fileItem)

    f.close()  # 关闭文件
    print(rmFileName)
    listDir(fileDir="E:\work\client_QML_final2\Resources", year=2019)
    # del_emp_dir(path)
