import urllib.request

url="http://www.gzzjcj.cn/bin/awscer.asp"
downPath='D:\工作\增城网站安全监控\网站\广州珠江职业技术学院\日志/test.txt'#include the source name，not only path，"\\"the first is the escape character
urllib.request.urlretrieve(url,downPath)