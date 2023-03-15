#!/usr/bin/env python
#coding:utf-8


import pymongo
import os
import sys,getopt
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import threading
import time


path1 = os.getcwd() + '/right_txt/'
isExists=os.path.exists(path1)
if not isExists:
    os.makedirs(path1)
else:
    print("文件夹存在")

path2 = os.getcwd() + '/wrong_txt/'
isExists=os.path.exists(path2)
if not isExists:
    os.makedirs(path2)
else:
    print("文件夹存在")


#lock = threading.Lock()

def create_text_right(name , msg):
    name = name.replace(":" , "_")
    full_path = path1 + '/' + name + '.txt'
    #print(full_path)
    file = open(full_path , 'w')
    file.write(msg)


def create_text_wrong(name , msg):
    name = name.replace(":" , "_")
    full_path = path2 + '/' + name + '.txt'
    #print(full_path)
    file = open(full_path , 'w')
    file.write(msg)

def check(line):

    #lock.acquire()
    r1 = open('wrong.txt','a+')
    r2 = open('right.txt','a+')
    
    try:
        
        url = line.strip('\n')
        com = "mongodb://" + url + "/"
        myclient = pymongo.MongoClient(com)
        dblist = myclient.list_database_names()

        #print(dblist)

    except Exception as e:
        #访问有问题的站点保存在error.txt
        with open('error.txt','a+') as ERR:  
            ERR.write(line.strip()+ '\n')
            myclient.close()
            #lock.release()

            
    else:
        if "READ_ME_TO_RECOVER_YOUR_DATA" in dblist:
            print(url + ":网站被勒索" + '\n')
            r1.write(line) 
            mydb = myclient["READ_ME_TO_RECOVER_YOUR_DATA"]
            mycol = mydb["README"]
            url_info = "数据库地址：" + line
            db_info = "数据库信息：" + str(dblist)
            lesuo_info = "勒索信息：" + str(mycol.find_one())
            info = url_info + db_info + '\n' + lesuo_info
            namex = str(url)
            create_text_wrong(namex , info)
            myclient.close()
            #lock.release()

        else:
            url_info = "数据库地址：" + line
            db_info = "数据库信息：" + str(dblist)
            info = url_info + db_info
            namex = str(url)
            create_text_right(namex , info)
            r2.write(line)
            print(url + ":网站正常" + '\n')
            myclient.close()
            #lock.release()

    
    
if __name__ == "__main__":
    
    threadPool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="check_")
    
    with open('url.txt','r') as f:
        
        for line in f.readlines():

            threads = threadPool.submit(check,line)

        threadPool.shutdown(wait=True)
        print('main finished')


        



