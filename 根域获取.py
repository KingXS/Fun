import sys, getopt
import tldextract

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

    with open(inputfile,'rb') as f:
        for line in f.readlines():
            print(line)
            #判断文本是否是二进制格式
            if str(type(line)) == bytetype:
                line = line.decode()
            else:
                pass

            try:
                print(line)
                ext = tldextract.extract(line.strip('\n'))
            except:
                pass
            else:
                print('.'.join(ext[:2]))

if __name__ == "__main__":
   change(sys.argv[1:])
