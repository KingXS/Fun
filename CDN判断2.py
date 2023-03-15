import sys
import dns.resolver
from urllib.parse import urlparse
import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor #线程池，进程池
import threading,time

#检查网站是否可以访问
def check_url(url):
    #print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko','Connection':'close'}
    try:
        #请求网站URL，获取状态码
        r = requests.get(url=url,headers=headers,timeout=4)
        #print(url)
        if isinstance(r.status_code,int):
            #print(r.status_code)
            return True
        else:
            return False
    except Exception as e:
        return False

#
def get_ip(url):
    ip = " "
    ip_list = []
    try:
        A = dns.resolver.resolve(url,'A')
    except Exception as e:
        print("dns resolver error:"+str(e))
    else:
        for i in A:
            ip_list.append(i)
            ip = i
        if len(ip_list) > 1:
            return True,ip
        else:
            return False,ip

#从文件中批量读取url进行判断
def checkcdn(url):         
    if check_url(url):
        try:
            url = url
            url1 = str(urlparse(url).hostname)
            yn,ip = get_ip(url1)
            if yn:
                with open('cdnurl.txt','a+') as r1:
                    url = url + "\n" 
                    r1.write(url)
                print(url.strip('\n'))
            else:
                with open('nocdnurl.txt','a+') as r2:
                    url = url + "\n"
                    r2.write(url)
                print(url.strip('\n'))
        except Exception as e:
            print(str(e))
    else:
        url = str(urlparse(url).hostname)
        print(url + "   网站无法访问")


if __name__ == '__main__':
    filename = sys.argv[1]
    thread_pool = ThreadPoolExecutor(5) #定义5个线程执行此任务
    process_pool = ProcessPoolExecutor(5) #定义5个进程
    with open(filename,'r') as f:
        for line in f.readlines():
            url = line.strip('\n')
            thread_pool.submit(checkcdn,url)





