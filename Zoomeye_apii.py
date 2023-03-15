import requests,json
import re
from urllib import parse
import sys, getopt


headers={
     'API-KEY':'EF1A0321-A5E7-c254a-9843-58eeff43b3e'
}

def api(argv):
    query = ""  #查询语句
    page = 0    #需要爬取的页数
    p = open('result.txt','w',encoding='utf-8')  #用于保存不重复的结果
    output = []

    try:
        opts, args = getopt.getopt(argv, "hq:p:", ["query=", "page="])
    except getopt.GetoptError:
        print ('test.py -q <query> -p <page>')
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -q <query> -p <page>')
            sys.exit()
        elif opt in ("-q", "--query"):
            query = arg
            print(query)
        elif opt in ("-p", "--page"):
            page = arg
            print(page)

    query = parse.quote_plus(str(query))
 
    for i in range(int(page)):
        urls = "https://api.zoomeye.org/host/search?query=" + query + "&page=" + str(i)
        print(urls)
        r = requests.get(url = urls,headers = headers)
        content = json.loads(r.text)
        a = content.get('matches')         #a的数据类型是列表
        c = 0
        banners = []   #用于保存banner信息的列表
        for item in a:

            #print(item)         #item的数据类型是字典
        
            for key in item:
                banners.append(item['portinfo']['banner'])
                d = item['portinfo']['banner'].split('\r\n') #将banner信息按照换行符进行分割并保存在列表d中
                for i in d:
                    if "Location" in i:
                        print(i.split("Location: ")[1]) #截取URL部分
                        urlresult = i.split("Location: ")[1]
                        if urlresult not in output:
                            output.append(urlresult)
    #将结果保存到文本中
    for i in output:
        p.write(i+'\r')
                        


if __name__ == "__main__":
   api(sys.argv[1:])

#for item in content.items():
#     print(item)


#print(type(content))

#content = json.dumps(r.text,sort_keys=True, indent=4, separators=(', ', ': '))

#content.get('matches')是匹配到的结果
#print(type(content.get('matches')))

#print(content.get('matches'))

#print(content)









 
          #print(re.findall(r'[Location: ](.*?)[\r\n]', item['portinfo']['banner']))
          #print("\n")
          #for line in item['portinfo']['banner']:
          #     print(line)
          #print(item['portinfo']['banner'])
          # 
#print(banners)
#print(c)


#匹配中间的字符串
#re.findall(r'[Location:](.*?)[\r\n]', str1)