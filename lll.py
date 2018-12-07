 #时间模块
#import time
# print(time.time())                                  #时间戳   从公元1970年到现在经历的秒
# print(time.localtime())                #本地时间  元组   默认显示当前时间  参数：填时间戳
# print(time.localtime(1540025315))
# print(time.strftime('%Y %m %d %H-%M-%S %w',time.localtime())) #将本地时间格式化成现代化时间

#a=time.strptime('1970 12 12','%Y %m %H')#将现代化的时间格式化成本地时间
#print(a )
# a=time.strptime('1970 12 12','%Y %m %H')            #将元祖的时间转换成时间戳
# print(time.mktime(a))
# b=(1978,12,12,12,23,33,3,123,0)                      #必须有九位，后三位无意义
# print(time.mktime(b))

# time.sleep(2)   #休眠
# print(123)

#输入一个现代化时期（年月日）1
# 输出，今年是否为闰年，今天是星期几，今天是一年中的第几天
# import time
# def nianyue(a):
#     d=a.split(' ')
# def riqi(a,b,c):
#     d=time.strptime('{} {} {}'.format(a,b,c),'%Y %m %d')
#     e=d[0]
#     if e % 4 ==0 and e%100 != 0 or e%400==0:
#         print(e, '是闰年')
#         print('星期', d[-3] + 1)
#         print('今天是第', d[-2], '天')
#     else:
#         print(e,'不是闰年')
#         print('星期',d[-3]+1)
#         print('今天是第',d[-2],'天')
# riqi(2018,10,24)

#爬虫
# import re
# import requests
# url='https://www.qiushibaike.com/'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'}
# adc=requests.get(url=url,headers=head)
# html=adc.content.decode('utf-8')
# #print(html)
# req=re.compile('<div class="content">(.*?)</span>',re.S)
# patt=req.findall(html)
# print(patt)
# for  i,j  in  enumerate(patt):
#     new_j=j
#     reqq=requests.get(new_j)
#     tu=reqq.content
#     with open(r'C:\Users\幸存者\Desktop\{}.jpg'.format(i), 'wb') as f:
#              f.write(tu)


# import xlrd    txt导入文档
# a=xlrd.open_workbook('vv.xls')
# sheet=a.sheets()[0]
# a=sheet.nrows
# for i in range(a):
#     g=sheet.row_values((i))
#     print(g)
#     with open('xx.txt','a+',encoding='utf-8') as f:
#         f.write('{} {} {}\n'.format(g[0],g[1],g[2]))



import time
a=input('请输入年月日')
c=a.split(' ')
b=time.strptime('{} {} {}'.format(int(c[0]),int(c[1]),int(c[2])),'%Y %m %d')
if b[0]%4==0 and b[0]%100!=0 or b[0]%400==0:
    print('今年是瑞年{},是这一年的第{}天，星期{}'.format(b[0],b[-2],b[-3]+1))
else:
    print('今年不是是瑞年{},是这一年的第{}天，星期{}'.format(b[0], b[-2], b[-3] + 1))
