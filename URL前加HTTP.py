#!/usr/bin/env python
#coding:utf-8

from socket import gethostbyname
import sys, getopt

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
            if "http" in line:
                with open(outputfile,'a+') as r:
                    r.write(line.strip('\n')+'\n')
            #else:
             
              #   line = "http://" + line
               # with open(outputfile,'a+') as r:
                #    r.write(line.strip('\n')+'\n')
            
            else:
                if "443" in line:
                    line = "https://" + line
                    with open(outputfile,'a+') as r:
                        r.write(line.strip('\n')+'\n')
                else:
                    line = "http://" + line
                    with open(outputfile,'a+') as r:
                        r.write(line.strip('\n')+'\n')


            



if __name__ == "__main__":
   change(sys.argv[1:])