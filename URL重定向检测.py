import sys
import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor #线程池，进程池
import threading,time
from bs4 import BeautifulSoup as bs   #将模块重命名
from concurrent.futures import ThreadPoolExecutor,wait
from lxml import etree

def check(url):
    url = url + "/////baidu.com"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    r = requests.get(url = url,headers = headers , allow_redirects=True)
    soup=str(bs(r.content,'lxml'))
    page = etree.HTML(soup)
    web_title = page.xpath("/html/head/title/text()")
#    print(web_title)
    if "百度一下" in str(web_title):
        print(url + "   存在URL跳转漏洞")
    else:
        pass

if __name__ == '__main__':
    filename = sys.argv[1]
    thread_pool = ThreadPoolExecutor(5) #定义5个线程执行此任务
    process_pool = ProcessPoolExecutor(5) #定义5个进程
    with open(filename,'r') as f:
        for line in f.readlines():
            url = line.strip('\n')
            thread_pool.submit(check,url)