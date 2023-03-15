import datetime
import urllib.request
import time
from urllib import request

def create_assist_date(datestart = None,dateend = None):
	# 创建日期辅助表

	if datestart is None:
		datestart = '2016-01-01'
	if dateend is None:
		dateend = datetime.datetime.now().strftime('%Y-%m-%d')

	# 转为日期格式
	datestart=datetime.datetime.strptime(datestart,'%Y-%m-%d')
	dateend=datetime.datetime.strptime(dateend,'%Y-%m-%d')
	date_list = []
	date_list.append(datestart.strftime('%Y-%m-%d'))
	while datestart<dateend:
		# 日期叠加一天
	    datestart+=datetime.timedelta(days=+1)
	    # 日期转字符串存入列表
	    date_list.append(datestart.strftime('%Y-%m-%d'))
	#print(date_list)
	return date_list


if __name__ == '__main__':
	dates = create_assist_date("2017-12-30","2019-09-03")


#	response = request.urlopen("http://www.gzzjcj.cn/log/log2017-12-30.txt")
#	html = response.read()
#	html = html.decode("utf-8")
#	print(html)

	for i in dates:
		try:
			filename = "log"+i+'.txt'
			print(filename)
			url="http://www.gzzjcj.cn/log/"+filename
			downPath='D:\工作\增城网站安全监控\网站\广州珠江职业技术学院\日志/'+filename#include the source name，not only path，"\\"the first is the escape character
			urllib.request.urlretrieve(url,downPath)
			time.sleep(8)
		except:
			continue


