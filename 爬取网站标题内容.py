import requests
from bs4 import BeautifulSoup as bs   #将模块重命名
from concurrent.futures import ThreadPoolExecutor,wait
from lxml import etree
import pymysql

#headers头部里面需要加上close，否则开启太多会导致无法再建立新连接
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko','Connection':'close'}
#counts = 0
#打开文件并按行读取
for line in open("passurl.txt","r"): #设置文件对象并读取每一行文件
    #print(line)
    url = line.strip() # 定义URL
    print(url)
    try:
        r = requests.get(url=url, headers=headers,timeout = 4,verify=False)  # 请求目标网址
        soup=str(bs(r.content,'lxml'))  #利用BS解析网址,因为etree模块只识别字符串，所以需要转化
        page = etree.HTML(soup) #建立etree树
#获取标题
        web_title = page.xpath("/html/head/title/text()")

        print(web_title)
        with open('result.txt', 'a+') as r:  # result.txt里面存储的是批量解析后的结果
            r.write(line.strip('\n') + ' ')  # 显示有ip绑定的域名，用空格隔开
            r.write(str(web_title) + '\n')
    except:
        with open('error.txt', 'a+') as r:  # result.txt里面存储的是批量解析后的结果
            r.write(line.strip('\n') + ' ')  # 显示有ip绑定的域名，用空格隔开
            r.write("出现错误" + '\n')



