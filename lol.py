import requests
import re
import os
import requests
import urllib.request
import json
import wget
import time
import sys

def root():
    download_munber = 0
    data_cishu = 1
    cishu_1 = 0
    print("涩图下载器 v1.0")
    print("使用 Github 源")
    print("-----分区-----")
    print("1.大部分正常二次元图片")
    print("2.原神")
    print("3.P站(不是P***hub)")
    print("4.猫娘")
    print("5.东方project")
    choose = input("选择:")
    file = input("输出路径:")
    if file == "":
        print("使用默认路径: C:\imgs")
        if os.path.exists('c:\imgs') == False:
            os.makedirs('c:\imgs')
            file = "C:\imgs"
    else:
        if os.path.exists(file) == False:
            choose2 = input("没有这个路径(" + file +")\n需要创建这个文件夹吗?(Yes or No)")
            if choose2 == "Yes":
                os.makedirs(file)
            elif choose2 == "No":
                pass
            elif choose2 == "yes":
                os.makedirs(file)
            elif choose2 == "no":
                pass
            else:
                pass
    if choose == "1":
        cishu = int(input("数量:"))
        for i in range(cishu):
            print("图片" + str(i))
            target_name = str(i) + '.jpg'
            os.system("curl -L https://api.r10086.com/img-api.php?type=%E5%8A%A8%E6%BC%AB%E7%BB%BC%E5%90%881 -o " + file + "\\" + str(i) + ".jpg")
        print("***下载成功awa***")
    if choose == "2":
        cishu = int(input("数量:"))
        for i in range(cishu):
            print("图片" + str(i))
            target_name = str(i) + '.jpg'
            os.system("curl -L https://api.r10086.com/img-api.php?zsy=%E5%8E%9F%E7%A5%9E -o " + file + "\\" + str(i) + ".jpg")
        print("***下载成功awa***")
    if choose == "3":
        cishu = int(input("数量:"))
        for i in range(cishu):
            print("图片" + str(i))
            target_name = str(i) + '.jpg'
            os.system("curl -L https://api.r10086.com/img-api.php?type=P%E7%AB%99%E7%B3%BB%E5%88%971' -o " + file + "\\" + str(i) + ".jpg")
        print("***下载成功awa***")
    if choose == "4":
        cishu = int(input("数量:"))
        for i in range(cishu):
            print("图片" + str(i))
            target_name = str(i) + '.jpg'
            os.system("curl -L https://api.r10086.com/img-api.php?type=%E7%8C%AB%E5%A8%981 -o " + file + "\\" + str(i) + ".jpg")
        print("***下载成功awa***")
    if choose == "5":
        cishu = int(input("数量:"))
        for i in range(cishu):
            print("图片" + str(i))
            target_name = str(i) + '.jpg'
            os.system("curl -L https://api.r10086.com/img-api.php?type=%E4%B8%9C%E6%96%B9project1 -o " + file + "\\" + str(i) + ".jpg")
        print("***下载成功awa***")
while True:
    root()