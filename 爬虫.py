# import re
# import requests
# url='https://www.doutula.com/'
# head={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# response=requests.get(url=url,headers=head)
# html=response.content.decode('UTF-8')
# patt=re.compile(r'<a href="(.*?)" class="tips">')
# patt1=re.compile(r'')
# items=patt.findall(html)
# for i,j in enumerate(items):
    # with open(r'C:\Users\幸存者\{}.jpg'.format(items[i]),'w',encoding='UTF-8')as f:
    #     f.write(j)

import requests
import re
url='https://www.yeitu.com/tag/xiurenwang/'
res=requests.get(url=url)
html=res.content.decode('utf-8')
patt=re.compile(r'><img src="(.*?)" alt="秀人网" /></a>')
items=patt.findall(html)
print(items)
# for i,j in enumerate(items):
#     mew_url = j
#     respons=requests.get(url=mew_url)
#     tu=respons.content
#     with open(r'‪C:\Users\幸存者\Desktop\大侄子\{}.jpg'.format(i), 'wb')as f:
#                     f.write(tu)
#


# import requests     #用函数爬去多张图片
# import re
# class Baisi():
#     # def __init__(self,head):
#     #     self.head=head
#     def qingqiu(self,page):
#         url = 'http://www.doutula.com/article/list/?page={}'.format(page)
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#         response = requests.get(url=url,headers=head)
#         html = response.content.decode('UTF-8')
#
#         return html
#     def guolv(self,html):
#         patt = re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
#         items = patt.findall(html)
#         # for i in items:
#             # print(i)
#         return items
#     def save(self,items):
#         qq = 0
#         for i in items:
#             print(i)
#             head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#             aaa = requests.get(url=i,headers=head)
#             html1 = aaa.content.decode('UTF-8')
#             patt1 = re.compile('onerror="this.src=(.*?)">',re.S)
#             items1 = patt1.findall(html1)
#             for i in items1:
#                 i=i.replace("'","")
#                 tupian = requests.get(i)
#                 res1 = tupian.content
#                 with open('{}.jpg'.format(qq),'wb') as f:
#                     f.write(res1)
#                 qq+=1
# a=Baisi()
# aa=a.qingqiu(1)
# b=a.guolv(aa)
# a.save(b)




#
# import time
# a=input('请输入时间')
# a=a.split(' ')
# b=time.strptime('{},{},{}'.format(a[0],a[1],a[2]),'%Y,%m,%d')
# if int(b[0])%4==0 and int(b[0])%100 !=0  or int(b[0])%400==0:
#     print('这是瑞年,是这一年的{}天，星期{}'.format(b[-2],b[-3]+1))
# else:
#     print('这不是瑞年,是这一年的{}天，星期{}'.format(b[-2],b[-3]+1))


# import requests
# import re
# url='http://www.biquge.com.tw/0_748/'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# adc=requests.get(url=url,headers=head)
# html=adc.content.decode('gbk')
# patt=re.compile('<dd><a href="(.*?)">',re.S)
# itmes=patt.findall(html)
# print(itmes)
# for i in itmes:
#     i_new=i
#     i_new='http://www.biquge.com.tw'+i_new
#     adc=requests.get(i_new)
#     htmll=adc.content.decode('gbk')
#     pattll=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</div>',re.S)
#     itmesl=pattll.findall(htmll)
#     print(itmesl)
#     with open('ff.txt','a+',encoding='gbk') as f:
#         f.write(itmesl[0])
#




# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# c=int(input('闹够了没有'))
# t=''
# while True:
#     d=c%16
#     c=c//16
#     t+=a[d]
#     if c==0:
#         break
# print(t[::-1])

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end=' ')
#     print(' ')



#
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('0.0.0.0',233))
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     msg='断剑重铸之日骑士归来之时'
#     s.sendto(msg.encode('utf-8'),b)


# 什么是测试用例   为了验证软件是否符合用户需求而编写的一组包括前置条件 测试输入 输出结果的等一系列集合
#缺陷 软件中
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('0.0.0.0',233))
# s.listen(5)
# while True:
#     a,d=s.accept()
#     meg=a.recv(1024)
#     print(meg.decode('utf-8'))
#     rsg='niadsd'
#     a.send(rsg.encode('utf-8'))


