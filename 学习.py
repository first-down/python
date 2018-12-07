
# txt导数据库
# import pymysql
# adc=pymysql.connect(host='192.168.0.123',
#                     port=3306,
#                     user='root',
#                     password='123456',
#                     charset='utf8')
# f=adc.cursor()
# f.execute('show databases;')
# f.execute('use text')
# with open('x.txt','r+',encoding='utf-8') as  t:
#     y=t.readlines()
# f.execute('create table biao129(姓名 char(100),年级  char(100),年龄 char(100));')
# for i in y:
#     if i[0]=='姓名' :
#         f.execute('create table biao129({} char(100),{}  char(100),{} char(100));'.format(i[0],i[1],i[2]))
#     else:
#         i=i.replace('\n','')
#         i=i.split(' ')
#         f.execute('insert into biao129 values("{}","{}","{}");'.format(i[0],i[1],i[2]))
# f.execute('select * from biao119;')
# j=f.fetchall()
# print(j)

#数据库导到xls
#   f.execute('create table biao11(y[] '
#  f.execute('desc wr')
# b=f.fetchall()
# print(b)
# f.execute('select * from wr;')
# a=f.fetchall()
# print(a)
# ad=xlwt.Workbook(encoding='utf-8')
# sheet=ad.add_sheet('第一个')
# for i in range(3):
#     sheet.write(0,i,b[i][0])
# for i in range(len(a)):
#     sheet.write(i+1,0,a[i][0])
#     sheet.write(i+1,1,a[i][1])
#     sheet.write(i+1,2,a[i][2])
# ad.save('k.xls')

#txt导xls表
# import xlwt
# with open('x.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# g=xlwt.Workbook()
# sheet=g.add_sheet('txt转入xls')
# for j,i in enumerate(a):
#     i=i.replace('\n','')
#     c=i.split()
#     sheet.write(j,0 , c[0])
#     sheet.write(j,1 , c[1])
#     sheet.write(j,2 , c[2])
# g.save('vv.xls')


#xls导数据库
# import xlwt
# import pymysql
# import xlrd
# f=xlrd.open_workbook('vv.xls')
# sheet=f.sheets()[0]
# a=sheet.nrows  #显示有多少行
# print(a)
# uu=[]
# c=sheet.row_values(0)  #显示第一行的内容
# for i in range(a):
#     t=sheet.row_values(i)
#     print(t)
#     uu.append(t)
# print(uu)
# adc=pymysql.connect(host='192.168.0.123',   #连接数据库
#                     port=3306,
#                     user='root',
#                     password='123456',
#                     charset='utf8')
# f=adc.cursor()
# f.execute('use text;')
# #for i in uu:
#     #if i[0]=='姓名':
#       #  f.execute('create table  yy11({} char(100),{}  char(100),{}  int );'.format(i[0],i[1],i[2]))
#    # else:
#        #1 f.execute('insert into  yy11  values("{}","{}","{}");'.format(i[0],i[1],i[2]))
# f.execute('select * from yy11;')
# pp=f.fetchall()
# f.execute('desc yy11;')
# ii=f.fetchall()
# print(pp)
# print(ii)





#txt导xls表
# import xlwt
# with open('xxx.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# g=xlwt.Workbook()
# sheet=g.add_sheet('123')
# for j,i in enumerate(a):
#     i=i.replace('\n','')
#     c=i.split()
#     sheet.write(j,0 , c[0])
#     sheet.write(j,1 , c[1])
#     sheet.write(j,2 , c[2])
# g.save('rr.xls')


# import xlrd    xls导入文档
# a=xlrd.open_workbook('vv.xls')

# sheet=a.sheets()[0]
# a=sheet.nrows
# for i in range(a):
#     g=sheet.row_values((i))
#     print(g)
#     with open('xx.txt','a+',encoding='utf-8') as f:
#         f.write('{} {} {}\n'.format(g[0],g[1],g[2]))






# import requests
# import re
# class Excel:
#     def __init__(self,p):
#         self.page=p
#     shuming=[]
#     def qingqiu(self):
#         url='https://book.douban.com/top250?start={}'.format(self.page)
#         res=requests.get(url=url)
#         html=res.content.decode('utf-8')
#         return html
#     def sming(self):
#         patt=re.compile(r'title="(.*?)"',re.S)
#         items_1=patt.findall(self.qingqiu())
#         for i in items_1:
#             if '可试读' in i:
#                 continue
#             else:
#                 self.shuming.append(i)
#         return self.shuming
#     def zjia(self):
#         txt=xlrd.open_workbook('shu.xls')
#         new_txt=copy(txt)
#         sheet=new_txt.add_sheet('diyiyen')
#         sheet.write(0,0,'书名')
#         sheet.write(0,0,'简介')
#         for  i,j in enumerate(self.sming()):
#             sheet.write(i+1,0,j)
#         for n,m in enumerate(self.jjie()):
#             sheet.write(n+1,1,m)
#         new_txt.save('shu.xls')
# a=Excel()
# b=a.qingqiu()
# c=b.zjia()
# print(c)


# import re
# import requests
# url='https://www.doutula.com/article/detail/4318023'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# rets=requests.get(url=url,headers=head)
# html=rets.content.decode('UTF-8')
# print(html)
# rrr=re.compile("this.src='(.*?)'",re.S)
# fe=rrr.findall(html)
# print(fe)
# for j,i in enumerate(fe):
#     tt=i.replace("'","")
#     rr=requests.get(tt)
#     htmll=rr.content
#     with open('{}.jpg'.format(j),'wb') as  f:
#         f.write(htmll)


#数据库导入xls
# import pymysql
# import xlwt
# adc=pymysql.connect(host='192.168.0.123',
#                     port=3306,
#                     user='root',
#                     password='123456',
#                     charset='utf8')
# a=adc.cursor()
# a.execute('show databases;')
# a.execute('use text;')
# a.execute('select * from yy11;')
# b=a.fetchall()
# a.execute('desc yy11;')
# c=a.fetchall()
# a=xlwt.Workbook(encoding='utf-8')
# sheet=a.add_sheet('s忽聚酷')
# for i in range(len(c)):
#     sheet.write(0,i,c[i][0])
#     for j in range(len(b)):
#         sheet.write(j+1,i,b[j][i])
# a.save('aa.xls')

# 数据库导txt
# import pymysql
# adc=pymysql.connect(host='192.168.0.123',port=3306,user='root',password='123456',charset='utf8')
# a=adc.cursor()
# a.execute('show databases;')
# a.execute('use text;')
# a.execute('select * from yy11;')
# b=a.fetchall()
# a.execute('desc yy11;')
# c=a.fetchall()
# print(c)
# with open('tt.txt','w+',encoding='utf-8') as f :
#     f.write('{},{},{}\n'.format(c[0][0],c[1][0],c[2][0]))
#     for i in b:
#         f.write('{},{},{}\n'.format(i[0],i[1],i[2]))

#
# import xlrd
# import pymysql
# adc=pymysql.connect(host='192.168.0.123',port=3306,user='root',password='123456',charset='utf8')
# a=adc.cursor()
# ttt=xlrd.open_workbook('rr.xls')
# sheet=ttt.sheets()[0]
# a=sheet.row_values((0))
# b=sheet.nrows
# for  i  in range(b):
#     t=sheet.row_values((i))
#     if i[0]=='姓名':
#         a.execute('create table  mkf({} char(100),{}   char(100),{} int );'.format(i[0],i[1],i[2]))
#     else:
#         a.execute('insert table mkf  values({} {} {});'.format(i[0],i[1],i[2]))
# adc.commit()

# import xlrd    xls导入文档
# a=xlrd.open_workbook('vv.xls')

# sheet=a.sheets()[0]
# a=sheet.nrows
# for i in range(a):
#     g=sheet.row_values((i))
#     print(g)
#     with open('xx.txt','a+',encoding='utf-8') as f:
#         f.write('{} {} {}\n'.format(g[0],g[1],g[2]))

# import pymysql
# adc=pymysql.connect(host='192.168.0.38',port=3306,user='root',password='123456',charset='utf8')



# import requests    #爬虫
# import re
# url='https://www.doutula.com/article/detail/9919451'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# ads=requests.get(url=url,headers=head)
# html=ads.content.decode('UTF-8')
# gg=re.compile("this.src='(.*?)'",re.S)
# itmes=gg.findall(html)
# print(itmes)
# for j,i in enumerate(itmes):
#     tt=requests.get(i)
#     htmll=tt.content
#     with open('{}.jpg'.format(j),'wb') as f:
#         f.write(htmll)


# import time     # 输出一个时间显示它是否是瑞年 是这一年的第几天 星期几
# a=input('请输入年月日')
# c=a.split(' ')
# b=time.strptime('{} {} {}'.format(int(c[0]),int(c[1]),int(c[2])),'%Y %m %d')
# if b[0]%4==0 and b[0]%100!=0 or b[0]%400==0:
#     print('今年是瑞年{},是这一年的第{}天，星期{}'.format(b[0],b[-2],b[-3]+1))
# else:
#     print('今年不是是瑞年{},是这一年的第{}天，星期{}'.format(b[0], b[-2], b[-3] + 1))



# import os     #判断文件类型
# a=os.listdir()
# for i in a:
#     if os.path.isfile(i):
#         print('{}普通文件'.format(i))
#     elif os.path.isdir(i):
#         print('{}目录文件'.format(i))
#     elif os.path.islink(i):
#         print('{}链接文件'.format(i))

# def zhishu(a,b):       #面向对象  任意范围的质数之和
#     s=0
#     for i in range(a,b):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             s+=i
#     return(s)
# print(zhishu(2,100))




#继承他的对象  阶乘之和

# def zhishu(seif,q,b):
#     s=0
#     t=1
#     for i  in range(q,b+1):
#         t=t*i
#         s+=t
#     return(s)
# print(zhishu(2,5))
#

#
#
# #面向对象    调用类的时候传入参数
# if  __name__=='__main__'



# a=input('<<<')
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)
# print(type(s))


# import socket            udp的socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',233)
# soc.bind(a)
# while True:
#     a,b=soc.recvfrom(1024)
#     print(a.decode('utf-8'))
#     rsg='你说的什么'
#     soc.sendto(rsg.encode('utf-8'))


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



# for i in range(1,10):     #九九乘法表
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end=' ')
#     print()




#a.txt中读取excel表格
# import xlwt
# def duqu():
#     with open('xxx.txt','r+',encoding='utf-8') as f:
#         b=f.readlines()
#     adc=xlwt.Workbook(encoding='utf-8')
#     sheet=adc.add_sheet('sheet1')
#     for j,i in enumerate(b):
#         i=i.replace('\n','')
#         a=i.split(' ')
#         print(a)
#         for h in range(len(a[0])+1):
#             sheet.write(j,h,a[h])
#     adc.save('yy.xls')
# duqu()




#保证所有的浏览器在同一环境下测试
#设置浏览器的大小
#设置浏览器的位置



# # dr.quit()  # 关闭浏览器
# #获取网站的标题  （title）
# print(dr.title)    #通常用来做断言的
# #获取网站的网址
# print(dr.current_url)   # 请求的网址与获取的网址是否一样
#设置浏览器的大小
# dr.set_window_size(400,400) #设置浏览器的大小  第一个是宽 第二个是高
# sleep(2)
# #设置浏览器打开对的位置
# dr.set_window_position(500,500)
# dr.maximize_window()   #把浏览器最大化
# dr.minimize_window()  #把浏览器最小化

# sleep(2)
# #浏览器的前进和后退
# dr.get('https://www.jd.com')
# sleep(3)
# dr.back()  #后退
# sleep(3)
# dr.forward()  #前进

from selenium  import webdriver
from time import sleep
dr = webdriver.Chrome()  # 打开浏览器
dr.get('http://www.baidu.com')   #请求的网址
#通过id属性来定位 定位到id=kw的位置
# dr.find_element_by_class_name('kw').send_keys('美女')

# sleep(2)
# dr.find_element_by_id('su').click()
# dr.quit()  # 关闭浏览器

#通过class属性定位
# dr.find_element_by_class_name('s_ipt').send_keys('霉霉')
# dr.find_element_by_class_name('bg s_btn').click()

#通过name属性来定位
dr.find_element_by_name('wd').send_keys('百度贴吧')
dr.find_element_by_id('su').click()
# dr.find_element_by_class_name('').click()
# # dr.find_element_by_name()



