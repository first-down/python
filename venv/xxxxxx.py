import smtplib  #发送邮件的协议
import email.mime.text  #处理发送的内容
import email.mime.multipart  #处理邮件的表头

sender='xcz201807@163.com'  #发送者
recver='m15037109541@163.com'
server='smtp.163.com'    # 服务器的地址    smtp.163.com 网易邮箱的服务器地址
passwd='shenme123'    #授权码
#创建一个空邮件
message=email.mime.multipart.MIMEMultipart()
#发件人
message['from']=sender
#收件人
message['to']=recver    #‘，’.join（recver）  这个是可以发送多个
#主题
message['subject']='如果有一天我变得很有钱'
#正文
text="""
天不生我李淳罡 剑道万古如长夜
"""
#处理文本信息
text=email.mime.text.MIMEText(text)
#将处理后的信息添加到邮件里
message.attach(text)
#定义服务器和端口
smtp123=smtplib.SMTP_SSL(server,465)
#登录服务器
smtp123.login(sender,passwd)
#发送邮件
smtp123.sendmail(sender,recver,message.as_string())
#断开连接
smtp123.close()



