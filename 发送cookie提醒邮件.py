import smtplib
import time
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def sendemail():
#sender是邮件发送人邮箱，passWord是服务器授权码，mail_host是服务器地址（这里是QQsmtp服务器）
    sender = 'brianxspe@163.com'#
    passWord = 'VHGOQUSWAWWADOTI'
    mail_host = 'smtp.163.com'
#receivers是邮件接收人，用列表保存，可以添加多个
    receivers = ['2532998854@qq.com']

#设置email信息
    msg = MIMEMultipart()
#邮件主题
    msg['Subject'] = "新cookie接收提醒"
#发送方信息
    msg['From'] = sender
#邮件正文是MIMEText:
    msg_content = "有新的cookie,注意查看"



#登录并发送邮件
    try:
    #QQsmtp服务器的端口号为465或587
        s = smtplib.SMTP_SSL("smtp.163.com",465)
        s.set_debuglevel(1)
        s.login(sender,passWord)
    #给receivers列表中的联系人逐个发送邮件
        for item in receivers:
            msg['To'] = to = item
            s.sendmail(sender,to,msg.as_string())
            print('Success!')
        s.quit()
        print ("All emails have been sent over!")
    except smtplib.SMTPException as e:
        print ("Falied,%s",e)

def sendmessage():
    filename = "cookie.txt"
    #print(type(time.time()))
    info = os.stat(filename)
    a = info.st_mtime

    while True:
        info = os.stat(filename)
        if a == info.st_mtime:  #10分钟
            continue
        else:
            sendemail()
            a = info.st_mtime


if __name__ == "__main__":
    sendmessage()