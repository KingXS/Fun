import requests
from bs4 import BeautifulSoup as bs   #将模块重命名
from concurrent.futures import ThreadPoolExecutor,wait
from lxml import etree
import pymysql
import time

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor #线程池，进程池
import threading,time

def test(arg):
    print(arg,threading.current_thread().name)
    time.sleep(1)
 
if __name__ == "__main__":
    thread_pool = ThreadPoolExecutor(5) #定义5个线程执行此任务
    process_pool = ProcessPoolExecutor(5) #定义5个进程
    for i in range(20):
        thread_pool.submit(test,i)
        #process_pool.submit(test,i)

url = "http://angemo.com/"
#headers头部里面需要加上close，否则开启太多会导致无法再建立新连接
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko','Connection':'close'}
#counts = 0
#打开文件并按行读取
for line in open("666.txt","r"): #设置文件对象并读取每一行文件
    time.sleep(2)
    #print(line)
    dir = line.strip() # 定义目录
    
    url = url + dir
    print(url)
    try:
        r = requests.get(url=url, headers=headers,timeout = 4,verify=False)  # 请求目标网
        if r.status_code = 200 and r.content