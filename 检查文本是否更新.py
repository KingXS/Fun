import os
import time

filename = "test.txt"
print(type(time.time()))
info = os.stat(filename)
a = info.st_mtime

while True:
    info = os.stat(filename)
    if a == info.st_mtime:  #10分钟
        continue
    else:
        print("文件已经更新")
        a = info.st_mtime
        