from socket import gethostbyname
import sys, getopt
import json

def change(argv):
    #获取参数
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            #用于保存要处理的结果
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            #保存输出的结果
            outputfile = arg

    output = []     #定义列表，保存结果
    strx = "["   #要截取的字符


    with open(inputfile,encoding='UTF-8') as fp:
        lines=fp.readlines()
        for i in lines:

            data = json.loads(i)  #转换为列表类型
            for i in data:
              
                x = i[0]
                print(x)
            
            
                output.append(x)
    with open(outputfile,'w',encoding='utf-8') as fp1:
        for i in output:
            fp1.write(i+'\n')

if __name__ == "__main__":
   change(sys.argv[1:])