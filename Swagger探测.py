import requests
from bs4 import BeautifulSoup as bs   #将模块重命名
from concurrent.futures import ThreadPoolExecutor,wait
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor,wait
from lxml import etree
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor #线程池，进程池
import threading,time
import urllib3
urllib3.disable_warnings()



def crawel(url):
    #headers头部里面需要加上close，否则开启太多会导致无法再建立新连接
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko','Connection':'close'}
    for line in open("Swagger.txt","r"):
        line = line.strip('\n')
        url = url + line

        print(url)
        try:
            r = requests.get(url=url, headers=headers,timeout = 4,verify=False)  # 请求目标网址
            soup=str(bs(r.content,'lxml'))  #利用BS解析网址,因为etree模块只识别字符串，所以需要转化
            page = etree.HTML(soup) #建立etree树

            if r.status_code == 200:

                f = open('Swagger_url.csv','a',newline='', encoding='utf-8-sig')
                csv_writer = csv.writer(f)

                csv_writer.writerow([url,"200状态码"])

            else:
                pass

        except:
            print(url.strip('\n') + ' ' + "出现错误" + '\n')


if __name__ == "__main__":
    thread_pool = ThreadPoolExecutor(30) #定义5个线程执行此任务
    process_pool = ProcessPoolExecutor(30) #定义5个进程
    with open('url.txt','r') as f:
        for line in f.readlines():
            url = line.strip('\n')
            thread_pool.submit(crawel,url)


