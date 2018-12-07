#  tcp
# # # serrver 端
# import socket
#
# # 创建一个socket  ,封装协议(第一个ipv4协议，第二个使用的tcp的协议)
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip和端口号   bind接收的参数是元组
# a=('0.0.0.0',233)     #3种方式  192  127   默认地址 0.0.0.0
# s.bind(a)
# #监听  数字指的是  最大等待数
# s.listen(123)
# while True:
#     a,b=s.accept()   #接收请求   产生两个结果
#                     # a是客户端的连接信息     b是客户端的IP地址和端口号
#     msg=a.recv(1024)  #接收数据     1024 每次接收的最大字节数
#     print(msg.decode('utf-8'))
#     #发送响应
#     reg='我于杀戮之中绽放亦如黎明中的花朵'
#     a.send(reg.encode('utf-8'))




# import socket
# # 创建一个socket  ,封装协议(第一个ipv4协议，第二个使用的udp的协议)
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定ip和端口号   bind接收的参数是元组
# a=('0.0.0.0',233)     #3种方式  192  127   默认地址 0.0.0.0
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)    #接收数据   第一个变量：客户端发送的请求数据     第二个变量：客户端的IP地址和端口号
#     print(a.decode('utf-8'))
#     print(b)
#     #发送响应数据
#     msg='生与死 轮回不止 他们生我们死'
#     s.sendto(msg.encode('utf-8'),b)




# import pymysql
# adc=pymysql.connect(host='192.168.0.38',
#                     port=3306,
#                     user='root',
#                     password='123456',
#                     charset='utf8')
# f=adc.cursor()
# f.execute('show databases;')
# f.execute('use xcz')
# with open('x.txt','r+',encoding='utf-8') as  t:
#     y=t.readlines()
# for i in y:
#     print(i)
#     if i[0]=='姓名' :
#         f.execute('create table zzyy({} char(100),{}  char(100),{} char(100));'.format(i[0],i[1],i[2]))
#     else:
#         i=i.replace('\n','')
#         i=i.split(' ')
#         f.execute('insert into biao129 values("{}","{}","{}");'.format(i[0],i[1],i[2]))
# f.execute('select * from biao119;')
# j=f.fetchall()
# print(j)


# import xlwt
# with open('x.txt','r+',encoding='utf-8') as f:
#     b=f.readlines()
# for i in b:
#     i=i.








#  #      邮件中添加附件发送
# import smtplib  #发送邮件的协议
# import email.mime.text  #处理发送的内容
# import email.mime.multipart  #处理邮件的表头
#
# sender='xcz201807@163.com'  #发送者
# recver='doungln@163.com'
# server='smtp.163.com'    # 服务器的地址    smtp.163.com 网易邮箱的服务器地址
# passwd='shenme123'    #授权码
# #创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
# #发件人
# message['from']=sender
# #收件人
# message['to']=recver    #‘，’.join（recver）  这个是可以发送多个
# #主题
# message['subject']='如果有一天我变得很有钱'
# #正文
# text="""
# 淑芬看你的邮箱
# """
# #处理文本信息
# text=email.mime.text.MIMEText(text)
# #将处理后的信息添加到邮件里
# message.attach(text)
#
# #添加附件： 处理附件：以二进制的方式读取文件
# att2=email.mime.text.MIMEText(open('one.jpg','rb').read(),'base64','utf-8')
# att2["Content-Type"]='application/octet-stream'
# att2["Content-Disposition"]='attachment;filename="abc.jpg"'
# #定义服务器和端口
# smtp123=smtplib.SMTP_SSL(server,465)
# #登录服务器
# smtp123.login(sender,passwd)
# #发送邮件
# smtp123.sendmail(sender,recver,message.as_string())
# #断开连接
# smtp123.close()








# import os
# a=os.listdir(r'g:/')
# for i in a:
#     if os.path.isfile(i):
#         print(i,'是普通文件')
#     else:
#         print(i,'不是普通文件')






#输入文件名  统计多少行，去掉空行，‘#’
# import os
# def hang(a):
#     for i in a:
#         s=0
#         d=0
#         if i=='\n' or i.startswith=='#':
#             s+=1
#         else:
#             d+=1
#     return(d)
# hang('0.txt')


#读取excel表格  第十三到二十行的内容
# import xlrd
# a=xlrd.open_workbook('aa.xls')
# sheet=a.sheets()[0]
# for i in range(5,11):
#     b=sheet.row_values((i))
#     print(b)


#
# a=input('请输入')
# b=a[::-1]
# s=0
# for i,j  in  enumerate(b):
#     for h in range(10):
#         if j==str(h):
#             s+=h*10**i
# print(type(s))


# for i in range(1,10):    #九九乘法表
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end=' ')
#     print(' ')


# def zhishu(a,b):    质数之和
#     s=0
#     for i in range(a,b):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             s+=i
#     return(s)
# print(zhishu(2,100))


# def jiecheng(a,b):    #阶乘之和
#     s=1
#     h=0
#     for i in range(a,b+1):
#        s=s*i
#        h+=s
#     return(h)
# print(jiecheng(1,5))

# def sanjiao(a,b,c):     #判断三角形
#     if a+b>c:
#         if a**2+b**2==b**2:
#             print('直角三角形')
#         elif a**2+b**2<b**2:
#             print('钝角三角形')
#         elif a**2+b**2>b**2:
#             print('锐角三角形')
#     else:
#         print('不是三角形')
# sanjiao(3,3,3)

#去重排序
# a=input('请输入')
# c=a.split(' ')
# b=[]
# for i in c:
#     if i not in b:
#         b.append(int(i))
#         b.sort()
# print(set(b))


#判断字符串是否回文
# a=input('请输入')
# b=a[::-1]
# if a==b:
#     print('这是回文')
# else:
#     print('这不是个回文')

class quanbu():    # 这个括号里面是集成其他的class  不能填写变量
    def __init__(self,b,a):   # 在class中 每个函数都可以继承   在这个def中写 的变量其他类中都可以继承
        self.b=b
        self.a=a
    def zhishu(self):    #  seif   类的实例化
        s=0
        for i in range(2,self.b+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                s+=i
        print(s)
    def jiujiu(self):
        self.zhishu()    #把一个class中的其他类  调用到本地类中
        for i in range(1,self.a):
            for j in range(1,i+1):
                print('{}*{}={}'.format(j,i,j*i),end=' ')
            print(' ')
# a=quanbu(100,10)
# a.jiujiu()
class dierge(quanbu):
    def asd(self):
        dierge.jiujiu()
a=dierge(100,9)
a.asd()
# class jicheng(quanbu):
#     print(123)
# c=jicheng()
# c.zhishu()