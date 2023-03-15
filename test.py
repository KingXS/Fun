import sys, getopt
import tldextract
from socket import gethostbyname
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor #线程池，进程池
import threading,time

bytetype = "<class 'bytes'>"

def change(argv):
    #获取参数
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", ""])
    except getopt.GetoptError:
        print ('test.py -i <inputfile>')
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    
    return inputfile,outputfile

    with open(inputfile,'rb') as f:
        for line in f.readlines():
            #print(line)
            #判断文本是否是二进制格式
            if str(type(line)) == bytetype:
                line = line.decode()
            else:
                pass

def get_domain(url,outputfile):
    try:
        #print(line)
        ext = tldextract.extract(url)
        domain = '.'.join(ext[1:])
        host = gethostbyname(domain)  #域名反解析得到的IP
        print(host)
    except:
        pass
    else:
        print(domain)
        with open(outputfile,'a+') as r: #result.txt里面存储的是批量解析后的结果
            #r.write(line.strip('\n') + ' ')   #显示有ip绑定的域名，用空格隔开
            r.write(domain + '\n')

if __name__ == "__main__":
    inputfile,outputfile = change(sys.argv[1:])
    thread_pool = ThreadPoolExecutor(5) #定义5个线程执行此任务
    process_pool = ProcessPoolExecutor(5) #定义5个进程
    with open(inputfile,'rb') as f:
        for line in f.readlines():
#判断文本中的字符格式是否为二进制格式
            if str(type(line)) == bytetype:
                line = line.decode()
            else:
                pass

            url = line.strip('\n')
            thread_pool.submit(get_domain,url,outputfile)



