import hashlib
import re
import sys
dicts = {}       #定义字典保存键值对
lists = []         #定义列表保存密码列表

#打开文件并按行读取其中的内容
with open('TOP1000.txt','r') as f :
    for line in f:
        #获取每一行的数据
        lists.append(list(line.strip('\n').split(',')))      #将每一行的数据添加到列表中



for i in lists:
    i = str(i)      #将列表类型的元素转化为字符串类型
    i = i.strip("['']")     #去掉字符串前后的 ['']
    key = bytes(i,encoding='utf-8') # 转换为bytes,编码为utf-8
    md5_value = hashlib.md5(key).hexdigest()        #创建md5对象并开始加密
    dicts[md5_value] = i        #将明文以及密文保存到字典中，密文对应明文

str = sys.argv[1]
a = dicts.get(str)
print(a)
    
