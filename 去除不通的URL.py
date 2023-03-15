#!/usr/bin/env python
#coding:utf-8


import requests
from socket import gethostbyname
import sys, getopt

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko','Connection':'close'}

def change(argv):
    #获取参数
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg


    with open(inputfile,'r') as f:

        for line in f.readlines():
            try:
                print(line)
                url = line.strip('\n')
                #请求网站URL，获取状态码
                r = requests.get(url=url, headers=headers)
            except Exception as e:
                with open('error.txt','a+') as ERR:  #error.txt为没有IP绑定的域名
                    ERR.write(line.strip()+ '\n')
            else:
                with open(outputfile,'a+') as r: #result.txt里面存储的是批量解析后的结果
                    r.write(line.strip('\n') + ' ')   #显示有ip绑定的域名，用空格隔开
                    r.write(host + '\n')


if __name__ == "__main__":
   change(sys.argv[1:])